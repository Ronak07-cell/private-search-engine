from urllib.robotparser import RobotFileParser
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urlunparse, parse_qs, urlencode

def get_robots_parser(start_url):
    parsed = urlparse(start_url)
    robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"

    rp = RobotFileParser()
    rp.set_url(robots_url)
    try:
        rp.read()
    except Exception:
        return None

    return rp

def normalize_url(url):
    parsed = urlparse(url)
    query_params = parse_qs(parsed.query)

    essential_params = {}
    if "page" in query_params:
        essential_params["page"] = query_params["page"]

    new_query = urlencode(essential_params, doseq=True)

    return urlunparse(parsed._replace(fragment="", query=new_query))

def crawl_page(url):
    print(f"Crawling: {url}")

    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
        return None, []

    if response.status_code != 200:
        print(f"Skipping {url} - status code {response.status_code}")
        return None, []
    
    soup = BeautifulSoup(response.text, "html.parser")

    page_text = soup.get_text(separator=" ", strip=True)

    links = []
    for link_tag in soup.find_all("a", href=True):
        full_url = urljoin(url, link_tag["href"])
        links.append(full_url)

    return page_text, links

def crawl_website(start_url, max_pages=10, same_domain_only=True):
    robots_parser = get_robots_parser(start_url)
    visited = set()
    to_visit = [normalize_url(start_url)]
    all_pages_data = []
    start_domain = urlparse(start_url).netloc

    

    while to_visit and len(visited) < max_pages:
        current_url = to_visit.pop(0)

        if current_url in visited:
            continue

        if robots_parser and not robots_parser.can_fetch("*", current_url):
            print(f"Skipping {current_url} - disallowed by robots.txt")
            continue

        text, links = crawl_page(current_url)
        visited.add(current_url)
        time.sleep(1)

        if text is None:
            continue

        all_pages_data.append({
            "url": current_url,
            "text": text
        })

        for link in links:
            normalized_link = normalize_url(link)

            if same_domain_only and urlparse(normalized_link).netloc != start_domain:
                continue

            if normalized_link not in visited:
                to_visit.append(normalized_link)

    return all_pages_data
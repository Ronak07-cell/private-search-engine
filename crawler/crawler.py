import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


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

def crawl_website(start_url, max_pages=10):
    visited = set()
    to_visit = [start_url]
    all_pages_data = []

    while to_visit and len(visited) < max_pages:
        current_url = to_visit.pop(0)

        if current_url in visited:
            continue

        text, links = crawl_page(current_url)
        visited.add(current_url)

        if text is None:
            continue

        all_pages_data.append({
            "url": current_url,
            "text": text
        })

        for link in links:
            if link not in visited:
                to_visit.append(link)

    return all_pages_data
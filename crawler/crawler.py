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
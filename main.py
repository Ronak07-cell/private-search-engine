from crawler.crawler import crawl_website

if __name__ == "__main__":
    start_url = "https://example.com"
    pages = crawl_website(start_url, max_pages=5)

    print(f"\n--- CRAWLED {len(pages)} PAGES ---")
    for page in pages:
        print(f"\nURL: {page['url']}")
        print(f"Text preview: {page['text'][:150]}")
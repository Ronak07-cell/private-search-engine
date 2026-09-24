from crawler.crawler import crawl_page

if __name__ == "__main__":
    test_url = "https://example.com"
    text, links = crawl_page(test_url)

    print("\n--- PAGE TEXT (first 300 characters) ---")
    print(text[:300])

    print("\n--- LINKS FOUND ---")
    for link in links:
        print(link)
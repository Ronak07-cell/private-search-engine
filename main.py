import json
from crawler.crawler import crawl_website
from indexer.indexer import load_pages, build_index, save_index

if __name__ == "__main__":
    start_url = "https://example.com"
    pages = crawl_website(start_url, max_pages=5)

    print(f"\n--- CRAWLED {len(pages)} PAGES ---")

    with open("data/crawled_pages.json", "w") as f:
        json.dump(pages, f, indent=2)

    print(f"Saved {len(pages)} pages to data/crawled_pages.json")

    pages_loaded = load_pages()
    index = build_index(pages_loaded)
    save_index(index)

    print(f"\n--- INDEX BUILT ---")
    print(f"Total unique words indexed: {len(index)}")

    sample_word = "domain"
    if sample_word in index:
        print(f"Pages containing '{sample_word}': {index[sample_word]}")
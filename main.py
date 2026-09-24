import json
from crawler.crawler import crawl_website
from indexer.indexer import load_pages, build_index, save_index
from search.search import load_index, search


def run_crawler_and_indexer():
    start_url = "https://example.com"
    pages = crawl_website(start_url, max_pages=5)

    with open("data/crawled_pages.json", "w") as f:
        json.dump(pages, f, indent=2)

    pages_loaded = load_pages()
    index = build_index(pages_loaded)
    save_index(index)

    print(f"Crawled {len(pages)} pages, indexed {len(index)} unique words.\n")


def run_search():
    index = load_index()
    pages = load_pages()

    while True:
        query = input("Search (or type 'exit' to quit): ")
        if query.lower() == "exit":
            break

        results = search(query, index, pages)

        if not results:
            print("No results found.\n")
            continue

        print(f"\nTop results for '{query}':")
        for url, score in results[:5]:
            print(f"  {score:.4f}  -  {url}")
        print()


if __name__ == "__main__":
    run_crawler_and_indexer()
    run_search()
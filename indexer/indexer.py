import json
import re
from collections import defaultdict


def load_pages(filepath="data/crawled_pages.json"):
    with open(filepath, "r") as f:
        pages = json.load(f)
    return pages


def tokenize(text):
    text = text.lower()
    words = re.findall(r"\b[a-z]+\b", text)
    return words


def build_index(pages):
    index = defaultdict(set)

    for page in pages:
        url = page["url"]
        words = tokenize(page["text"])

        for word in words:
            index[word].add(url)

    return index


def save_index(index, filepath="data/search_index.json"):
    index_as_lists = {word: list(urls) for word, urls in index.items()}

    with open(filepath, "w") as f:
        json.dump(index_as_lists, f, indent=2)
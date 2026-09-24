import json
import math
from indexer.indexer import tokenize


def load_index(filepath="data/search_index.json"):
    with open(filepath, "r") as f:
        index = json.load(f)
    return index


def load_pages(filepath="data/crawled_pages.json"):
    with open(filepath, "r") as f:
        pages = json.load(f)
    return pages


def compute_tf(word, page_text_tokens):
    if len(page_text_tokens) == 0:
        return 0
    word_count = page_text_tokens.count(word)
    return word_count / len(page_text_tokens)


def compute_idf(word, index, total_pages):
    pages_with_word = len(index.get(word, []))
    return math.log((total_pages + 1) / (pages_with_word + 1)) + 1


def search(query, index, pages):
    query_words = tokenize(query)
    total_pages = len(pages)

    scores = {}

    for page in pages:
        url = page["url"]
        page_tokens = tokenize(page["text"])

        page_score = 0
        for word in query_words:
            tf = compute_tf(word, page_tokens)
            idf = compute_idf(word, index, total_pages)
            page_score += tf * idf

        if page_score > 0:
            scores[url] = page_score

    ranked_results = sorted(scores.items(), key=lambda item: item[1], reverse=True)

    return ranked_results
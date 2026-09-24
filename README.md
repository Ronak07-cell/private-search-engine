# Private Search Engine

A search engine built completely from scratch in Python — no external search libraries used. Implements web crawling, inverted indexing, and TF-IDF ranking, the same core concepts behind real search engines.

## Features

- **Web Crawler**: Recursively crawls websites starting from a seed URL, following links up to a configurable depth
- **Inverted Index**: Maps every word to the set of pages containing it, enabling fast lookups
- **TF-IDF Ranking**: Scores and ranks search results by relevance using Term Frequency–Inverse Document Frequency, with smoothing to handle common terms
- **Interactive CLI**: Search crawled content directly from the terminal

## How it works

1. `crawler.py` fetches pages, extracts text and links, and follows those links to discover more pages
2. `indexer.py` builds an inverted index (word → pages) from all crawled content
3. `search.py` scores each page against a search query using TF-IDF and returns ranked results

## Setup

\`\`\`bash
git clone https://github.com/Ronak07-cell/private-search-engine.git
cd private-search-engine
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
\`\`\`

## Usage

\`\`\`bash
python3 main.py
\`\`\`

This crawls a seed site, builds the index, then drops you into an interactive search prompt.

## Tech Stack

- Python 3
- `requests` — HTTP fetching
- `BeautifulSoup4` — HTML parsing
- Custom TF-IDF implementation (no ML/search libraries used)

## What I learned

- How inverted indexes enable fast text search at scale
- TF-IDF scoring and why IDF smoothing is necessary in practice
- Handling real-world crawling issues: timeouts, broken links, relative URL resolution
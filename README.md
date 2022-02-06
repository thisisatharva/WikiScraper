# WikiScraper
WikiScraper performs a search on Wikipedia given a key word or a phrase, and provides the URL and summaries of the resulting articles. 

Wikiscraper uses the [MediaWiki Action API](https://www.mediawiki.org/wiki/API:Main_page) to perform searches and obtain data from Wikipedia.

## What wiki_scraper does ##
The process of getting url and summaries of articles occurs in two phases. First, we find a user defined "n" relevant articles given a keyword and return these article names in form of an array. Next, this array is passed on to the get_info function where each of the "n" articles are searched for and their URLs and extracts returned. 

## How to run wiki_scraper.py ##
The example out.json file provided was run using :

```zsh

python wiki_extractor.py --keyword="Indian Historical Events" --num_urls=10 --output="out.json"

```

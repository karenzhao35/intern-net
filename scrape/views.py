from django.shortcuts import render

# Create your views here.
import re
import json
from scrapfly import ScrapflyClient, ScrapeConfig

scrapfly = ScrapflyClient(key="scp-live-764641ae102e46e0a74641837f839c45")

def parse_search_page(html: str, limit: int = None):
    data = re.findall(r'window.mosaic.providerData\["mosaic-provider-jobcards"\]=(\{.+?\});', html)
    if not data:
        return None
    data = json.loads(data[0])
    
    results = data["metaData"]["mosaicProviderJobCardsModel"]["results"]
    if limit:
        results = results[:limit]

    return {
        "results": results,
        "meta": data["metaData"]["mosaicProviderJobCardsModel"]["tierSummaries"],
    }

result = scrapfly.scrape(
    ScrapeConfig(
        url="https://www.indeed.ca/jobs?q=software+intern&l=Canada",
        asp=True,
    )
)

# Example: limit to 5 items
print(parse_search_page(result.content, limit=5))

from django.http import HttpResponse
# Create your views here.
import re
import json
from scrapfly import ScrapflyClient, ScrapeConfig

scrapfly = ScrapflyClient(key="scp-live-764641ae102e46e0a74641837f839c45")

result = scrapfly.scrape(
    ScrapeConfig(
        url="https://www.indeed.ca/jobs?q=software+intern&l=Canada",
        asp=True,
    )
)


def parse_search_page(request):
    data = re.findall(r'window.mosaic.providerData\["mosaic-provider-jobcards"\]=(\{.+?\});', result.content)
    if not data:
        return None
    data = json.loads(data[0])
    
    results = data["metaData"]["mosaicProviderJobCardsModel"]["results"]
    results = results[:5]

    return HttpResponse(json.dumps({
        "results": results,
        "meta": data["metaData"]["mosaicProviderJobCardsModel"]["tierSummaries"],
    }), content_type="application/json")



# # Example: limit to 5 items
# print(parse_search_page())

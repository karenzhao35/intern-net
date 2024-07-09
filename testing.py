import httpx
from parse import Selector

response = httpx.get(
    "https://www.glassdoor.com/Overview/Working-at-eBay-EI_IE7853.11,15.htm"
)
selector = Selector(response.text)
# find description in the HTML:
print(selector.css('[data-test="employerDescription"]::text').get())
# will print:
# eBay is where the world goes to shop, sell, and give. Every day, our professionals connect millions of buyers and sellers around the globe, empowering people and creating opportunity. We're on a mission to build a better, more connected form of commerce that benefits individuals

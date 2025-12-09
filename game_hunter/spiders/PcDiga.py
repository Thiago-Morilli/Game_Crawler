import scrapy
import json


class GamehunterSpider(scrapy.Spider):
    name = "PcDiga"
    domains = "https://www.pcdiga.com/"

    def start_requests(self):
        trigger = (
            "P082860,P081676,P082582,P082566,P081285,P080969,P082864,"
            "P074610,P074296,P082731,P080115,P082581,P079998,P078883,"
            "P081907,P083000,P083302,P078873,P077042,P082599,P081090,"
            "P082743,P081084,P078262,P082579,P082862,P077044,P078869,P080655"
        )

        url = (
            "https://kjvn6r1caotq07dlp.a1.typesense.net/multi_search"
            f"?use_cache=true&trigger={trigger}"
        )

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
            "Content-Type": "application/json",
            "Origin": "https://www.pcdiga.com",
            "Referer": "https://www.pcdiga.com/",
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/142.0.0.0 Safari/537.36"
            ),
            "x-typesense-api-key": "SLlLtgm4Ot1cFCnJZunQlKbN4O6ln3tt",
        }

        payload = {
            "searches": [
                {
                    "q": "*",
                    "query_by": "categories",
                    "collection": "productCollectionProd",
                    "per_page": 48,
                    "filter_by": (
                        "refurbished_sku:=[] || sku:=[P082860,P081676,P082582,"
                        "P082566,P081285,P080969,P082864,P074610,P074296,"
                        "P082731,P080115,P082581,P079998,P078883,P081907,"
                        "P083000,P083302,P078873,P077042,P082599,P081090,"
                        "P082743,P081084,P078262,P082579,P082862,P077044,"
                        "P078869,P080655]"
                    ),
                    "page": 1,
                }
            ]
        }

        yield scrapy.Request(
            url=url,
            method="POST",
            headers=headers,
            callback=self.category,
            body=json.dumps(payload),
        )

    def category(self, response):
        print(response)

import scrapy


class GamehunterSpider(scrapy.Spider):
    name = "Chip7"
    domains = "https://chip7.pt/"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept": (
            "text/html,application/xhtml+xml,application/xml;"
            "q=0.9,image/avif,image/webp,*/*;q=0.8"
        ),
        "Accept-Language": "pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    }

    def start_requests(self):
        yield scrapy.Request(
            url=self.domains,
            method="GET",
            callback=self.category,
        )

    def category(self, response):
        link_category = response.xpath(
            '//div[@class="flex flex-col absolute top-2 w-full"]'
            '/div[@class="cursor-pointer hover:bg-gray-100 px-6 mx-2 py-2 flex justify-between text-gray-400"]/a/text()'
        ).get()
        yield scrapy.Request(
                url=self.domains + link_category,
                method="GET",
                callback=self.sub_category,
                headers=self.headers,
            )

    def sub_category(self, response):
        print(response)
        

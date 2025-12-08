import scrapy


class GamehunterSpider(scrapy.Spider):
    name = "Globaldata"
    domains = "https://www.pcdiga.com/"

    def start_requests(self):
        yield scrapy.Request(
            url=self.domains,
            method="GET",
            callback=self.category,
        )

    def category(self, response):
        print(response)

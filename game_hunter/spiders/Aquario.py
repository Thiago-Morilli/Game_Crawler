import scrapy


class GamehunterSpider(scrapy.Spider):
    name = "Aquario"
    domains = "https://www.aquario.pt/"

    def start_requests(self):
        yield scrapy.Request(
            url=self.domains,
            method="GET",
            callback=self.category,
        )

    def category(self, response):
        print(response)

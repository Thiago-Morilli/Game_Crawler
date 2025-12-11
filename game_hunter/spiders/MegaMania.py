import scrapy


class GamehunterSpider(scrapy.Spider):
    name = "MegaMania"
    domains = "https://www.mega-mania.com.pt/"

    def start_requests(self):
        yield scrapy.Request(
            url="https://www.mega-mania.com.pt/",
            method="GET",
            callback=self.category,
        )

    def category(self, response):
        for link_category in response.xpath(
            '//div[@class="main-menu-tabs"]/div[@class="main-menu-tabs-table"]/div/a/@href'
        ).getall():
            yield scrapy.Request(
                url=self.domains + link_category,
                method="GET",
                callback=self.sub_category,
            )

    def sub_category(self, response):
        link = response.xpath(
            '//div[@style="float: left; width: 100%; height: auto;"]/div/form/div'
            '/div[@class="produto_lista_titulo"]/p/a/@href'
        ).get()
        print(link)

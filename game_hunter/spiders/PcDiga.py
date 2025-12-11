import scrapy
import json


class GamehunterSpider(scrapy.Spider):
    name = "PcDiga"
    domains = "https://www.pcdiga.com"
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
    }

    def start_requests(self):
        yield scrapy.Request(
            url="https://www.aquario.pt/",
            method="GET",
            headers=self.headers,
            callback=self.category,
        )

    def category(self, response):
        print(response)
        for link_category in response.xpath(
            '//div[@class="swiper-slide"]/div/a/@href'
        ).getall():
            """yield scrapy.Request(
                url=self.domains + link_category,
                method="GET",
                headers=self.headers,
                callback=self.sub_category,
            )

    def sub_category(self, response):"""

import scrapy


class MonsterSpiderSpider(scrapy.Spider):
    name = "monster-spider"
    allowed_domains = ["monster.com"]
    start_urls = ["https://monster.com"]

    def parse(self, response):
        pass

import scrapy

class SpiderCia(scrapy.Spider):
    name = 'cia'
    start_urls = [
        "https://www.cia.gov/readingroom/historical-collections"
    ]

    custom_settings = {
        'FEED_URI':'cia.json',
        'FEED_FORMAT':'json',
        'FEED_EXPORT_ENCODING':'utf-8'
    }


    def parse(self, response):
        links_declasified = response.xpath('//a[starts-with(@href,"collection") and (parent::h3 or parent::h2)]/@href').getall()
        for link in links_declasified:
            print(link)
            yield response.follow(link, callback = self.parse_link)

    def parse_link(self, response):
        pass
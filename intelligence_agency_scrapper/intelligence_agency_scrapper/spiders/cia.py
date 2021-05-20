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
            yield response.follow(link, 
                                callback = self.parse_link,
                                cb_kwargs = { 
                                    'url': response.urljoin(link)
                                })


    def parse_link(self, response, **kwargs):
        link = kwargs['url']
        title = response.xpath('//h1[@class="documentFirstHeading"]/text()').get()
        paragrph = response.xpath('//div[@class="field-item even"]//p[not(@class)]/text()').getall()
        yield {
            'url':link,
            'title':title,
            'body': paragrph
        }

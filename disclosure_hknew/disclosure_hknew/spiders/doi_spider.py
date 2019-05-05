import scrapy


class DOISpider(scrapy.Spider):
    name = "doi"
    start_url = 'http://sdinotice.hkex.com.hk/di/NSSrchCorp.aspx?src=MAIN&lang=EN',
    # def start_requests(self):
    #     urls = [
    #         'http://sdinotice.hkex.com.hk/di/NSSrchCorp.aspx?src=MAIN&lang=EN',
    #
    #     ]
        # for url in urls:
        #     yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
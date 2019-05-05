import scrapy
import sys
# sys.path.insert(0, 'D:\project\scrapy_project\scrapy_tutorial\scrapy_tutorial')
# print(sys.path)
from scrapy_tutorial.scrapy_tutorial.items import ScrapyTutorialItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    # def start_requests(self):
    #     urls = [
    #         # 'http://quotes.toscrape.com/page/1/',
    #         # 'http://quotes.toscrape.com/page/2/',
    #         'http://sdinotice.hkex.com.hk/di/NSNotice3AListprint.aspx?sa2=nd&sid=6893&sd=04/05/2018&ed=04/05/2019&cid=0&sa1=cl&scsd=04%2f05%2f2018&sced=04%2f05%2f2019&src=MAIN&lang=EN&'
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)
    #
    # def parse(self, response):
    #     # page = response.url.split("/")[-2]
    #     # filename = 'quotes-%s.html' % page
    #     filename = 'hkexnew6893'
    #     with open(filename, 'wb') as f:
    #         # f.write(response.body)
    #         f.write(response.body)
    #     self.log('Saved file %s' % filename)
    start_urls = [
        # 'http://quotes.toscrape.com/page/1/',
        # 'http://quotes.toscrape.com/page/2/',
        'http://sdinotice.hkex.com.hk/di/NSNotice3AListprint.aspx?sa2=nd&sid=6893&sd=04/05/2018&ed=04/05/2019&cid=0&sa1=cl&scsd=04%2f05%2f2018&sced=04%2f05%2f2019&src=MAIN&lang=EN&'
    ]

    def parse(self, response):
        for sel in response.xpath('//*[@id="Table1"]/tbody/tr[5]/td[2]').getall():
            item = ScrapyTutorialItem()
            item['serial_name'] = sel.xpath('//*[@id="grdPaging"]/tbody/tr[2]/td[1]').extract()
            item['director_name'] = sel.xpath('//*[@id="grdPaging"]/tbody/tr[2]/td[2]').extract()

            yield {"serial_name": item['serial_name'], 'director_name': item['director_name']}

        # for href in response.xpath('//a/@href').getall():
        #     yield scrapy.Request(response.urljoin(href), self.parse)

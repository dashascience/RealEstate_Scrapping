# -*- coding: utf-8 -*-
import scrapy


class RealestateSpider(scrapy.Spider):
    filename = 'realestate.txt'
    name = 'realestate'
    allowed_domains = ['https://www.gumtree.pl']
    start_urls = ['https://www.gumtree.pl/s-nieruchomosci/katowice/mieszkanie+do+wynajecia/v1c2l3200285q0p1']

    def parse(self, response):
        price =response.css('.amount::text').extract()
        description = response.css('.description::text').extract()

        for item in zip(price, description):
            # create a dictionary to store the scraped info
            scraped_info = {
                'price': item[0],
                'description': item[1]
            }

            # yield or give the scraped info to scrapy
            yield scraped_info
        with open(self.filename, 'a+') as f:
            f.writelines(scraped_info)
        self.log('Saved file %s' % self.filename)

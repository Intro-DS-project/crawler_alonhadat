import scrapy
from crawler_alonhadat.items import AlonhdatItem
from datetime import date, timedelta
from bs4 import BeautifulSoup

class AlonhadatSpider(scrapy.Spider):
      name = 'alonhadat'
      allowed_domains = ['alonhadat.com.vn']
      start_urls = ['http://alonhadat.com.vn/']

      def start_requests(self):
            pages = []
            for i in range(1,10):
                  domain = 'https://alonhadat.com.vn/nha-dat/cho-thue/phong-tro-nha-tro/1/ha-noi/trang--{}.html'.format(i)
                  pages.append(domain)

            for page in pages:
                  yield scrapy.Request(url=page, callback=self.parse_link)

            # for url in urls:
            #     yield scrapy.Request(url=url, callback=self.parse_link)

      def parse_link(self, response):
            for i in range(1, 21):
                  str = '#left > div.content-items > div:nth-child({}) > div.ct_title_box > div.ct_title > a::attr(href)'.format(i)
                  link = response.css(str).extract_first()
                  link = 'https://alonhadat.com.vn/' + link

            yield scrapy.Request(url=link, callback=self.parse)
      def parse(self, response, **kwargs):
            item = AlonhdatItem()
            item['price'] = self.extract(response, '#left > div.property > div.moreinfor > span.price > span.value')
            item['area'] = self.extract(response, '#left > div.property > div.moreinfor > span.square > span.value')
         
            address = self.extract(response, '#left > div.property > div.address > span.value')
            address = address.split(', ')
            if len(address) :
                  item['street'] = address[-4]
                  item['ward'] = address[-3]
                  item['district'] = address[-2]

            #post_data
            item["post_date"] = self.extract(response, '#left > div.property > div.title > span', 'start_date')
            item['description'] = self.extract(response, '#left > div.property > div.detail.text-content')
            item['url'] = response.request.url
            
            #extract table
            item['num_floor'] = response.css('.property > .moreinfor1 > .infor > table > tr:nth-child(4) > td:nth-child(4)::text').extract_first()
            item['num_bedroom'] = response.css('.property > .moreinfor1 > .infor > table > tr:nth-child(5) > td:nth-child(4)::text').extract_first()
            item['num_diningroom'] = response.css('.property > .moreinfor1 > .infor > table > tr:nth-child(1) > td:nth-child(6) > img::attr(src)').extract_first()
            item['num_kitchen'] = response.css('.property > .moreinfor1 > .infor > table > tr:nth-child(2) > td:nth-child(6) > img::attr(src)').extract_first()
            item['street_width'] = response.css('.property > .moreinfor1 > .infor > table > tr:nth-child(2) > td:nth-child(4)::text').extract_first()
            item['direction'] = response.css('.property > .moreinfor1 > .infor > table > tr:nth-child(1) > td:nth-child(4)::text').extract_first()
            item['num_toilet'] = None
            yield item 

      def extract(self, response, query, para=None):
            query += "::text"
            model = response.css(query).extract_first()

            if model is not None:
                  # start_date and end_date, convert string => now datetime
                  if para == 'start_date' or para == 'end_date':
                        now = date.today().strftime("%d/%m/%Y")
                        pre = (date.today() - timedelta(1)).strftime("%d/%m/%Y")
                        return model.replace("Hôm qua", pre).replace("Hôm nay", now)

            return model
      

            



      





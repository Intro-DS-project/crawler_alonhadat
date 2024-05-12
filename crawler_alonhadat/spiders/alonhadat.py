import scrapy
from crawler_alonhadat.items import AlonhdatItem
from datetime import date, timedelta
from crawler_alonhadat.api import extract_description

from hanoikovoidcdau import standardize
from crawler_alonhadat.remote_database import init
import random

today = date.today().strftime("%d/%m/%Y")
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
]

class AlonhadatSpider(scrapy.Spider):
      name = 'alonhadat'
      allowed_domains = ['alonhadat.com.vn']
      start_urls = ['http://alonhadat.com.vn/']
      supabase = init()

      def start_requests(self):
            pages = []
            for i in range(1,3):
                  domain = 'https://alonhadat.com.vn/nha-dat/cho-thue/phong-tro-nha-tro/1/ha-noi/trang--{}.html'.format(i)
                  pages.append(domain)

            for page in pages:
                  user_agent = random.choice(user_agents)
                  yield scrapy.Request(url=page, callback=self.parse_link, headers = {'User-Agent': user_agent})



      def parse_link(self, response):
            for i in range(1, 21):
                  str = '#left > div.content-items > div:nth-child({}) > div.ct_title_box > div.ct_title > a::attr(href)'.format(i)
                  link = response.css(str).extract_first()
                  link = 'https://alonhadat.com.vn/' + link

                  yield scrapy.Request(url=link, callback=self.parse, headers = {'User-Agent': random.choice(user_agents)})
      def parse(self, response, **kwargs):
            item = AlonhdatItem()
            price = response.css('#left > div.property > div.moreinfor > span.price > span.value::text').extract_first()
            item['price'] = format_value(price)
            area = response.css('#left > div.property > div.moreinfor > span.square > span.value::text').extract_first()
            item['area'] = format_value(area)


         
            address = response.css('#left > div.property > div.address > span.value::text').extract_first()
            # lambda for check address none, if none ignore


            address = address.split(', ')
            if len(address) :
                    item['street'] = address[-4]
                    item['ward'] = address[-3]
                    item['district'] = address[-2]

            item["street"] = standardize.standardize_street_name(item["street"])
            item["ward"] = standardize.standardize_ward_name(item["ward"])
            item["district"] = standardize.standardize_district_name(item["district"])

            #post_data
            post_date = response.css('#left > div.property > div.title > span::text').extract_first()
            item['post_date'] = format_date(post_date)
            item["description"] = response.css("#left > div.property > div.detail.text-content::text").extract_first()
            item['url'] = response.request.url
            
            #extract table
            num_bedroom, num_diningroom, num_kitchen, num_toilet, num_floor, current_floor, direction, street_width = extract_description(item["description"]).split(",")
            item["num_bedroom"] = num_bedroom
            item["num_diningroom"] = num_diningroom
            item["num_kitchen"] = num_kitchen
            item["num_toilet"] = num_toilet
            item["num_floor"] = num_floor
            item["current_floor"] = current_floor
            item["direction"] = direction
            item["street_width"] = street_width
            # nếu post_dâte là hôm nay hoặc hôm qua thì mới lấy thông tin
            if item['post_date'] == today:
                  data, count = self.supabase.table("entries").insert(item.to_dict()).execute()
      
            yield item


      
def format_date(post_date):
      post_date = post_date.split(":")[1]
      post_date = post_date.strip()
      now = date.today().strftime("%d/%m/%Y")
      pre = (date.today() - timedelta(1)).strftime("%d/%m/%Y")
      if post_date == "Hôm nay":
            return now
      elif post_date == "Hôm qua":
            return pre
      else:
            return post_date
      

def format_value(value):
      return float(value.strip().split(" ")[0].replace(",", "."))



      
            



      





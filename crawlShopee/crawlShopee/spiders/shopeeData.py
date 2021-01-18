import scrapy
import json

from datetime import datetime
class crawlShopee(scrapy.Spider):
    name = 'reviews'
    allowed_domains = ['shopee.vn']
    start_urls = ['https://shopee.vn/api/v2/item/get_ratings?filter=0&flag=1&itemid=3355289986&limit=6&offset=0&shopid=69897724&type=0']

    def parse(self, response):
            #print(response.body)
            resp = json.loads(response.body)
            data = resp.get('data')
            ratings = data.get('ratings')
            for rating in ratings:
                    yield {
                            'username': rating.get('author_username'),
                            'comment': rating.get('comment')
                    }
                        #print(response.body)
            #url = 'https://shopee.vn/api/v2/item/get_ratings?filter=0&flag=1&itemid=4010229477&limit=6&offset=0&shopid=79711504&type=0'



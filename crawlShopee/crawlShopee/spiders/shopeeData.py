import scrapy
import json
from datetime import datetime

class crawlShopee(scrapy.Spider):
    name = 'reviews'
    allowed_domains = ['shopee.vn']
    idProduct = ['3355289986', '7659194604', '4460537443', '4737194401', '2261315595', '3215606112', '2759191741', '2693593903', '6230153207', '3445730232', '4659597711', '4359601176', '4559601186', '6369444354', '3617078926', '3640138830', '7502590024', '6365780389', '4450481893', '7353912449', '4339646384', '6247404150', '2854683877', '7363861807', '5537645743', '3914727869']
    idShop = ['69897724', '25452983', '65589552', '65589552', '44772106', '40757878', '188633', '65589552', '40757878', '115073315', '310737801', '310734832', '312004609', '107641355', '107641355', '2849350', '59404551', '30441763', '162554752', '217973472', '52809472', '131560988', '131560988', '134747469', '259348045', '77268672']
    offset = ['0', '6', '12', '18', '24', '30', '36', '42', '48', '54', '60', '66', '72']
    urls = []
    for i in range(len(idProduct)):
        for k in range(len(offset)):
            urls.append("https://shopee.vn/api/v2/item/get_ratings?filter=0&flag=1&itemid=" + idProduct[
                i] + "&limit=6&offset=" + offset[k] + "&shopid=" + idShop[i] + "&type=0")
    start_urls = urls

    def parse(self, response):
            #print(response.body)
            resp = json.loads(response.body)
            data = resp.get('data')
            ratings = data.get('ratings')
            for rating in ratings:
                    yield {
                            'Username': rating.get('author_username'),
                            'Comment': rating.get('comment'),
                            'Rating': rating.get('rating_star'),
                            'Time': datetime.fromtimestamp(rating.get('ctime')).strftime('%Y-%m-%d %H:%M:%S'),
                            'IdProduct': rating.get('itemid')
                    }
            with open('crawlShopee/crawlShopee/spiders/outputTMDT.txt', 'a', encoding='utf8') as f:
                    f.write(json.dumps(data, ensure_ascii=False))
                    f.write('\n')
                    print('SUCCESS:', response.url)

                        #print(response.body)
            #url = 'https://shopee.vn/api/v2/item/get_ratings?filter=0&flag=1&itemid=4010229477&limit=6&offset=0&shopid=79711504&type=0'



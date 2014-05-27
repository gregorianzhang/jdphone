# -*- coding: utf-8 -*-

from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from jdphone.items import JdphoneItem
import requests
import re
import json

class PhoneSpider(CrawlSpider):
    name = 'phone'
    allowed_domains = ['jd.com']
    start_urls = ['http://list.jd.com/9987-653-655-0-0-0-0-0-0-0-1-1-1-1-1-72-4137-33.html']

    rules = (
        Rule(SgmlLinkExtractor(allow=r'9987-653-655-0-0-0-0-0-0-0-1-1-\d+-1-1-72-4137-33.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
	items = []
        sel = Selector(response)
        #i['domain_id'] = sel.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = sel.xpath('//div[@id="name"]').extract()
        #i['description'] = sel.xpath('//div[@id="description"]').extract()
        phonelist = sel.xpath('//*[@class="list-h"]')
	purl = 'http://p.3.cn/prices/mgets?skuIds=J_'
	for num in xrange(36):
            i = JdphoneItem()
	    num = str(num)
	    
	    i['name'] = phonelist.xpath('//*[@index='+ num + ']//*[@class="p-name"]/a/text()').extract()
	    i['url'] = phonelist.xpath('//*[@index='+ num + ']//*[@class="p-name"]/a/@href').extract()
#            print "44444444444444444444444444444444444444"
#	    print i['name']
#            print num
## 京东价格是js合成的 所以单纯的抓取页面取不到数据了
	    pidre = re.compile(r'/(\d+)\.html',re.UNICODE)
	    pid = pidre.search(str(i['url']))
	    if pid:
	        pidnum = pid.group(1)

	    url = purl + pidnum
	    pricehtml = requests.get(url)
#	    print url
	    obj = json.loads(pricehtml.text)
	    i['price'] = obj[0]['p']
#	    print "1111111111111111111111111111111111111"
#   	    print  i['name'],i['price'],i['url']
#	    print i,items
#	    print "2222222222222222222222"
#	    print type(items)
#	    print items
	    items.append(i)
#	    print "3333333333333333333333333"
#	    print type(i)
#           print i
#	    print items
	
	return items



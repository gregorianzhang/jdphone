# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#class JdphonePipeline(object):
#    def process_item(self, item, spider):
#        return item

import re
from scrapy import log
from twisted.enterprise import adbapi
from scrapy.http import Request
from scrapy.exceptions import DropItem
from scrapy.contrib.pipeline.images import ImagesPipeline
#from qidian.items import QidianItem
from jdphone.items import JdphoneItem
import time
import MySQLdb
import MySQLdb.cursors

class MySQLStorePipeline(object):
    """docstring for MySQLstor"""
    def __init__(self):

        self.dbpool = adbapi.ConnectionPool('MySQLdb',
            host = '127.0.0.1',
            db = 'test',
            user = 'root',
            passwd = 'root',
            cursorclass = MySQLdb.cursors.DictCursor,
            charset = 'utf8',
            use_unicode = True
        )
    def process_item(self, item, spider):
	#print "aaaaaaaaaaaaaaaaaaaaaaaaaa"
        #print spider
        # run db query in thread pool
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)
#	print "0000000000000000000000000000000000000000000000000000"


        return item
    def _conditional_insert(self, tx, item):
        if item.get('name'):
         #   print "insert into phone (name, price, url) values (%s, %s, %s)" % (item['name'][0],item['price'][0],item['url'][0],)
	#    print "pric %s" % item['price']
            tx.execute("insert into phone (name, price, url) values (%s, %s, %s)",
                (item['name'][0],
                 item['price'],
                 item['url'][0],
                )
)
    def handle_error(self, e):
        log.err(e)


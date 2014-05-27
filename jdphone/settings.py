# Scrapy settings for jdphone project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'jdphone'

SPIDER_MODULES = ['jdphone.spiders']
NEWSPIDER_MODULE = 'jdphone.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'aaaa (+http://www.aa.com)'

ITEM_PIPELINES = {
	'jdphone.pipelines.MySQLStorePipeline': 345,
}

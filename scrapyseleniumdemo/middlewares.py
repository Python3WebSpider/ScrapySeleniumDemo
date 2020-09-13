# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse
from selenium import webdriver
import time


class SeleniumMiddleware(object):
    
    def process_request(self, request, spider):
        url = request.url
        browser = webdriver.Chrome()
        browser.get(url)
        time.sleep(5)
        html = browser.page_source
        browser.close()
        return HtmlResponse(url=request.url,
                            body=html,
                            request=request,
                            encoding='utf-8',
                            status=200)

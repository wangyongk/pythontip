import scrapy
from scrapy.selector import Selector
from dangdang.items import BookspiderItem
class bookSpider(scrapy.Spider):
    name = 'bookScrapy'
    #for i in range(1,26):
    start_urls = ['http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-%d'%i for i in range(1,26)]
        #start_urls = ['http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-%d'%i]
    def parse(self, response):
        item = BookspiderItem()
        sel = Selector(response)
        book_list = response.css('ul.bang_list.clearfix.bang_list_mode').xpath('li')
        for book in book_list:
            item['rank'] = book.css('div.list_num').xpath('text()').extract_first().strip('.')
            item['name'] = book.css('div.name').xpath('a/text()').extract_first()
            item['author'] = book.css('div.publisher_info')[0].xpath('a/text()').extract_first()
            item['press'] = book.css('div.publisher_info')[1].xpath('a/text()').extract_first()
            item['price'] = book.css('span.price_n').xpath('text()').extract_first()
            item['comments'] = book.css('div.star').xpath('a/text()').extract_first()
            yield item
import scrapy

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_cloud.items import ScrapyCloudItem


class PttMoviesSpider(CrawlSpider):
    name = 'ptt_movies'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/movie/index.html']

    rules = (
        Rule(LinkExtractor(
            restrict_xpaths="//div[@class='title']/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(
            restrict_xpaths="//div[@class='btn-group btn-group-paging']/a[2]"))
    )

    def parse_item(self, response):
        item = ScrapyCloudItem()
        # item['title'] = response.xpath(
        #     "normalize-space((//span[@class='article-meta-value'])[3]/text())").extract()
        # i['title'] = ''.join(title)
        for s in response.xpath("normalize-space((//span[@class='article-meta-value'])[3]/text())").extract():
            if "雷" in s:
                item['title'] = s

                item['author'] = response.xpath(
                    "(//span[@class='article-meta-value'])[1]/text()").extract()
                # i['author'] = ''.join(author)

                item['date'] = response.xpath(
                    "(//span[@class='article-meta-value'])[4]/text()").extract()
                # i['date'] = ''.join(date)

                item['contenttext'] = response.xpath(
                    "//div[@id='main-content']/text()").extract()

                yield item

            else:
                yield None

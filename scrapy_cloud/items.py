# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyCloudItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    contenttext = scrapy.Field()


class YahooCloudItem(scrapy.Item):
    title = scrapy.Field()
    critics_consensus = scrapy.Field()
    date = scrapy.Field()
    duration = scrapy.Field()
    genre = scrapy.Field()
    rating = scrapy.Field()
    amount_reviews = scrapy.Field()
    images = scrapy.Field()

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
import os
import re

from scrapy.pipelines.images import ImagesPipeline, FilesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request
from urllib.parse import urljoin

from datetime import datetime
from decimal import Decimal


def clean_title(param):
    return ''.join(param)


def clean_critics_consensus(param):
    return ''.join(param)


def clean_date(param):
    regex = '[^0-9]+'
    param = re.sub(regex, '', str(param))
    return ''.join(param)


def clean_duration(param):
    return ''.join(param)


def clean_genre(param):
    return ''.join(param)


def clean_rating(param):
    return ''.join(param)


def clean_images(param):
    return ''.join(param)


def clean_amount_reviews(param):
    regex = '[^A-Za-z0-9]+'
    param = re.sub(regex, '', str(param))
    return ''.join(param)


def clean_author(param):
    return ''.join(param)


def clean_contenttext(param):
    return ''.join(param)


class PttPipeline:
    def process_item(self, item, spider):
        item["title"] = clean_title(item["title"])
        item['author'] = clean_author(item['author'])
        item["date"] = clean_date(item["date"])
        item['contenttext'] = clean_contenttext(item['contenttext'])

        return item


class YahooPipeline:
    def process_item(self, item, spider):
        item["title"] = clean_title(item["title"])
        item["date"] = clean_date(item["date"])
        item["critics_consensus"] = clean_critics_consensus(
            item["critics_consensus"])
        item['duration'] = clean_duration(item["duration"])
        item['genre'] = clean_genre(item["genre"])
        item['rating'] = clean_rating(item["rating"])
        item['images'] = clean_images(item["images"])
        item['amount_reviews'] = clean_amount_reviews(item["amount_reviews"])

        return item


# class CustomImagePipeline(ImagesPipeline):

#     def get_media_requests(self, item, info):
#         # for (image_url, image_name) in zip(item['images'], item['title']):
#         #     yield scrapy.Request(url=image_url, meta={"image_name": image_name})
#         if 'images' in item:
#             for img_name, image_url in item['images'].items():
#                 request = scrapy.Request(url=image_url)
#                 new_img_name = ('%s.jpg' % (img_name)).replace(" ", "")
#                 request.meta['img_name'] = new_img_name
#                 yield request

#     def file_path(self, request, response=None, info=None):
#         return os.path.join(info.spider.IMAGE_DIR, request.meta['img_name'])


class DeleteNullTitlePipeline(object):
    def process_item(self, item, spider):
        title = item['title']
        if title:
            return item
        else:
            raise DropItem('found null title %s', item)


class DuplicatesTitlePipeline(object):
    def __init__(self):
        self.movie = set()

    def process_item(self, item, spider):
        title = item['title']
        if title in self.movie:
            raise DropItem('duplicates title found %s', item)
        self.movie.add(title)
        return(item)

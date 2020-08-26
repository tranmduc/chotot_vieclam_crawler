# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class Vieclam(Item):
    id = Field()
    url = Field()
    title = Field()
    salary = Field()
    tel = Field()
    district = Field()
    seller = Field()
    seller_type = Field()
    crawled_time = Field()
    posted_time = Field()
    salary_type = Field()
    job_field = Field()
    gender = Field()
    quantity = Field()
    certi_skill = Field()
    max_age = Field()
    job_type = Field()
    experience = Field()
    company = Field()
    education = Field()
    min_age = Field()
    bonus = Field()
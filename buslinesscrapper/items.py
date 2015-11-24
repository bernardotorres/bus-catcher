# -*- coding: utf-8 -*-

import scrapy


class LineItem(scrapy.Item):
    origin = scrapy.Field()
    weekday = scrapy.Field()
    times = scrapy.Field()


class BusRouteItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    duration = scrapy.Field()
    last_change = scrapy.Field()
    price_money = scrapy.Field()
    price_card = scrapy.Field()
    timetable = scrapy.Field()
    itinerary = scrapy.Field()

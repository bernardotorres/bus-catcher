# -*- coding: utf-8 -*-
from __future__ import print_function
from buslinesscrapper.items import BusRouteItem, LineItem
import scrapy
import re
import sys
from scrapy.http import Request


class FenixSpider(scrapy.Spider):
    name = "fenix"
    allowed_domains = ["www.consorciofenix.com.br"]
    start_urls = (
        'http://www.consorciofenix.com.br/horarios/',
    )

    def parse_line(self, response):
        bus_line = BusRouteItem()
        bus_line['url'] = response.url
        periods = []
        information = response.xpath('//*[@id="conteudo"]/div/div[1]/div[1]')
        line_name = information.xpath('//*[@id="conteudo"]/div/div[1]/h1/a/text()').extract()[0]
        timetable = []
        for row in response.xpath("//div[@class='row']"):
            li = LineItem()
            title = row.xpath(".//h4[@class='title4']/text()").extract()
            if title == []:
                continue
            title = title[0]
            name, origin = re.match(r"^([^-]*) - Sa\xedda (.*)$", title).groups()
            li['weekday'] = name
            li['origin'] = origin
            times = []
            # is a line with a timetable
            for x in row.xpath(".//*[@data-semana]"):
                hour = int(x.xpath('.//@data-horario').extract()[0])
                times += ["%04d" % hour]
            li['times'] = times
            # TODO: get times with special conditions (adapted vehicle, etc)
            timetable += [li]
        bus_line['timetable'] = timetable
        bus_line['name'] = line_name
        bus_line['duration'] = information.xpath('div[1]/text()[4]').extract()[0]
        bus_line['last_change'] = information.xpath('div[1]/text()[6]').extract()[0]
        bus_line['price_card'] = information.xpath('div[2]/div[1]/text()[3]').extract()[0]
        bus_line['price_money'] = information.xpath('div[2]/div[1]/text()[5]').extract()[0]
        stops = []
        for stop in response.xpath('//*[@id="conteudo"]/div/div[1]/ol/li/text()'):
            stops += [stop.extract()]
        bus_line['itinerary'] = stops
        return bus_line

    def parse(self, response):
        for link in response.xpath("//a/@href").extract():
            if link.find(",") != -1:
                url = "http://www.consorciofenix.com.br/horarios/%s" % link
                yield Request(url, callback=self.parse_line)

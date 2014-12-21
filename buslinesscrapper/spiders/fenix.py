# -*- coding: utf-8 -*-
from collections import OrderedDict
import scrapy
import re
from scrapy.http import Request


class FenixSpider(scrapy.Spider):
    name = "fenix"
    allowed_domains = ["www.consorciofenix.com.br"]
    start_urls = (
        'http://www.consorciofenix.com.br/horarios/',
    )

    def parse_line(self, response):
        periods = []
        name = response.xpath('//*[@id="conteudo"]/div/div[1]/h1/a/text()').extract()[0]
        for row in response.xpath("//div[@class='row']"):
            origin = row.xpath(".//h4[@class='title4']/text()").extract()
            if len(origin) > 0:
                # is a line with a timetable
                times = [("%04d" % int(x.xpath('.//@data-horario').extract()[0]), x.xpath('.//@data-semana').extract()[0]) for x in row.xpath(".//*[@data-semana]")]
                periods += [(origin[0], times)]
        for origin, times in periods:
            byHour = OrderedDict()
            print "LINHA", name
            print "ORIGEM %s" % origin
            print "SAÍDAS:"
            for time, dow in times:
                timeMatch = re.match("^([0-9]{2})([0-9]{2})$", time)
                hour, minute = timeMatch.groups(0)
                if not byHour.has_key(int(hour)):
                    byHour[int(hour)] = []
                byHour[int(hour)].append(minute)
            out = ""
            for hour, minutes in byHour.iteritems():
                out += "%02d:" % hour
                for minute in minutes:
                    out += " %s" % minute
                out += "\n"
            print out

    def parse(self, response):
        for link in response.xpath("//a/@href").extract():
           if link.find(",") != -1:
               url = "http://www.consorciofenix.com.br/horarios/%s" % link
               yield Request(url, callback=self.parse_line)

# -*- coding: utf-8 -*-
import unicodedata
import re
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from collections import OrderedDict
import json


SPACE_BETWEEN_LINES = 16
SPACE_BETWEEN_COLUMNS = 20
TIMETABLE_FONT_SIZE = 12
PLANS_DIRECTORY = "time_plans/"
URL_TO_FILENAME = r"^.*/(?P<name>.*),(?P<code>D*-*[0-9]*)"
NORMALIZE_NAME = r"^(?P<name>.*) - (?P<code>D*-*[0-9]*)$"


def stem_and_leaf(times):
    byHour = OrderedDict()
    for hour in range(5, 24):
        byHour[hour] = []
    for time in times:
        timeMatch = re.match("^([0-9]{2})([0-9]{2})$", time)
        hour, minute = timeMatch.groups(0)
        if int(hour) not in byHour:
            byHour[int(hour)] = []
        byHour[int(hour)].append(minute)
    return byHour


# Shortens some line names for reading clarity
shortenings = {
    u'TICAN - Terminal Integra\xe7\xe3o Canasvieiras': "TICAN",
    'Mercado Magia': "Merc. Magia"
}


def get_shortened(name):
    return shortenings.get(name, name)


def get_normalized_filename(url):
    filename_dict = re.match(URL_TO_FILENAME, url).groupdict()
    print filename_dict
    return PLANS_DIRECTORY + "{name}_{code}.pdf".format(**filename_dict)


def create_pdf(item):
    name_match = re.match(NORMALIZE_NAME, item["name"])
    line_name, line_code = name_match.groups()
    filename = get_normalized_filename(item['url'])
    c = canvas.Canvas(filename, pagesize=landscape(A4))

    # draw a rectangle
    c.setFillColorRGB(0, 0, 0)
    c.setFontSize(36)
    c.drawString(45, 550, line_name)
    c.setFillColorRGB(0.7, 0.7, 0.7)
    c.rect(45, 378, 715, 40, stroke=1, fill=1)
    c.setFillColorRGB(0, 0, 0)

    linex = 20
    c.setFontSize(TIMETABLE_FONT_SIZE)
    for line_num, time in enumerate(item['timetable']):
        x = linex
        y = 400
        origin_shortened = get_shortened(time['origin'])
        c.drawString(x + 45, 800 - y, origin_shortened)
        y += 12
        c.drawString(x + 45, 800 - y, time['weekday'])
        y += 12
        byHour = stem_and_leaf(time['times'])
        for n, time in enumerate(byHour.iteritems()):
            hour, minutes = time
            y += SPACE_BETWEEN_LINES
            x = linex
            c.setFillColorRGB(0.9, 0.9, 0.9)
            if n % 2:
                c.rect(x + 35, 800 - y - 3, 115, 14, stroke=0, fill=1)
            c.setFillColorRGB(0, 0, 0)
            if line_num == 0:
                c.drawString(x, 800 - y, "%02d:" % hour)
            x += SPACE_BETWEEN_COLUMNS
            for minute in minutes:
                x += SPACE_BETWEEN_COLUMNS
                c.drawString(x, 800 - y, " %s" % minute)
        linex += 120

    c.drawString(50, 800, item['name'])

    c.save()


class BusRoutePlanPipeline(object):

    def process_item(self, item, spider):
        create_pdf(item)
        return item

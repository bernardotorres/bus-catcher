# -*- coding: utf-8 -*-
import json
import pickle
import re
from collections import OrderedDict


def stem_and_leaf(times):
    byHour = OrderedDict()
    for time in times:
        timeMatch = re.match("^([0-9]{2})([0-9]{2})$", time)
        hour, minute = timeMatch.groups(0)
        if int(hour) not in byHour:
            byHour[int(hour)] = []
        byHour[int(hour)].append(minute)
    out = ""
    for hour, minutes in byHour.iteritems():
        out += "%02d:" % hour
        for minute in minutes:
            out += " %s" % minute
        out += "\n"
    print (out)


class BusRoutePrintPipeline(object):

    def process_item(self, item, spider):
        print("LINHA", item['name'])
        print("SAÍDAS:")
        for time in item['timetable']:
            print("ORIGEM %s" % time['origin'])
            for line in item['timetable']:
                stem_and_leaf(line['times'])
        return item

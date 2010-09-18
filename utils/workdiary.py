
import datetime, re
from dateutil import parser
import datetime

DATAFILE = '/home/src/notes/todo/wordcounts'

def extract_dates(fileobj):
    """
    lines are expected to be like:
    S Thu Sep  9 15:42:22 CEST 2010: 823 controllers/studio.py
    any where we can't find a date

    """
    dates = []
    lines = 0
    for line in fileobj:
        lines += 1
        try:
            datestr = line.split(': ')[0][2:]
            dates.append(parser.parse(datestr))
        except ValueError:
            pass
    print('found %s dates from %s lines' % (len(dates), lines))
    return dates

def get_wordcounts():
    return extract_dates(open(DATAFILE))

def checkins_per_hour(start, end, wordcounts):
    hourstart = start.replace(minute = 0, second = 0) #round hours
    if not hourstart.tzinfo:
        raise
    counts = [] #fill with tuples of (starttime, endtime, count)
    while hourstart < end:
        hourend = hourstart + datetime.timedelta(hours = 1)
        count = sum(1 for x in wordcounts if hourstart <= x < hourend)
        counts.append((hourstart, hourend, count))
        hourstart = hourend
    return counts

def checkins_per_day(whichday):
    """whichday can be datetime, or a string for dateutil"""
    if not isinstance(whichday, datetime.datetime):
        whichday = parser.parse(whichday)
    start = whichday.replace(hour = 0, minute = 0, second = 0)
    end = whichday.replace(hour = 23, minute = 59, second = 59)
    return checkins_per_hour(start, end, get_wordcounts())

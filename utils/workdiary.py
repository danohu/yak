
import datetime, re
from dateutil import parser

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

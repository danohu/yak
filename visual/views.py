# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
import glob, json, re
from collections import defaultdict
from markdown import markdown
from datetime import datetime, timedelta
from models import RecurringTask, RecurringTaskResult
import string

PROJECT_FILES = '/home/src/notes/todo/p*txt' #glob

project_sortorder = (
        'active', 'fading', 'inactive', 'on hold', 'paused',
        'unknown', 'completed', 'abandoned')

project_sortdict = dict(zip(project_sortorder, string.letters))



def asciiffs(brokenstring):
    """
    Like UnicodeDammit, but actually works. And breaks any non-ascii input.
    """
    return ''.join(x for x in brokenstring if ord(x) < 128)


def findjson(text):
    """
    input is a string possibly containing a json string somewhere within it
    look for it, parse the json. return the parsed json, or {} if it doesn't exist
    """
    match = re.search('({.*?})', text, re.DOTALL)
    if match is None:
        return {}
    try:
        return json.loads(match.group(1))
    except ValueError:
        return {}

def parselists(body):
    headings = ('TODO', 'NEXT', 'DONE')
    

@login_required
def do_task(request):
    date = request.GET.get('date', None)
    task_id = request.GET.get('task_id', None)
    result = request.GET.get('result', None)
    if not (date and result):
        return HttpResponse('Bad data')
    try:
        task = RecurringTask.objects.get(id = task_id)
    except ObjectDoesNotExist:
        return HttpResponse('No such task')
    try: #delete existing row
        dbrow = RecurringTaskResult.objects.get(date = date, task = task)
        dbrow.delete()
        return HttpResponse('Undone')
    except ObjectDoesNotExist:
        dbrow = RecurringTaskResult(date = date, task = task, result = task.max)
        dbrow.save()
    return HttpResponse(dbrow.result)
    

def todolist(body, howmany = 3):
    """XXX: this needs to also incorporate details from non-vim
    sources. i.e. probably will need to operate with a wider set
    of inputs
    Output is a list of todo items
    """
    parts = re.split('TODO', body, 1)
    if len(parts) < 2:
        return []
    results = []
    for line in parts[1].split('\n'):
        line = line.strip()
        if line:
            results.append(line)
        if len(results) >= howmany:
            break
    return results
    
    

def parse_textfile(filename):
    """handle the markup-plus thing, to get a usable object
    out of a plain text file"""
    data = defaultdict(str)
    textfile = open(filename, 'r')
    data.update({
        'filename' : filename,
        'title'    : textfile.readline().strip(),
        'status'   : 'unknown',})
    body = textfile.read()
    data['body_plain'] = body
    data['body_markdown'] = markdown(asciiffs(body))
    data['todoitems'] = todolist(body)
    data.update(findjson(body))
    data['sortorder'] = project_sortdict.get(data['status'], 'z')
    #XXX json should probably be removed from the remainder of the body
    return data

def get_projects():
    """XXX: probably want to bolt on some todo-list parsing here"""
    return [parse_textfile(x) for x in glob.glob(PROJECT_FILES)]
    


@login_required
def index(request):
    data = {'projects' : get_projects()}
    data.update(recurring_tasks())
    return render_to_response('dashboard.html', data) 

def dateify(predate):
    """
    turn a string containing a date into a datetime object
    if it is already a datetime object, return it unmodified
    return None for data we can't handle
    XXX: generalise this so it can handle all kinds of dates
    and get the strptime headache away from me
    """
    assert(isinstance(predate, (str, unicode, datetime)))
    if isinstance(predate, datetime):
        return predate
    formatstrings = ('%Y-%m-%d', '%Y')
    for formatstring in formatstrings:
        try:
            return datetime.strptime(predate, formatstring)
        except ValueError:
            continue
    return None


def daterange(startdate, enddate, step = None):
    """
    XXX: this should be in a utils library somewhere
    Return a list of dates between startdate and enddate, exclusively
    step is one day by default, but can be specified otherwise
    dates can be supplied as datetime.datetime or datetime.date
    """
    startdate, enddate = map(dateify, (startdate, enddate))
    if step is None:
        step = timedelta(days = 1)
    dates = []
    while startdate <= enddate:
        dates.append(startdate)
        startdate += step
    return dates



def recurring_tasks(request = None, startdate = None, enddate = None):
    enddate = enddate or datetime.now()
    startdate = startdate or (enddate - timedelta(days = 14))
    dates = daterange(startdate, enddate)
    dates.reverse()
    results = dict((x, []) for x in RecurringTask.objects.all())
    for date in dates:
        for result in results.keys():
            try:
                results[result].append(result.recurringtaskresult_set.get(date = date).result)
            except ObjectDoesNotExist:
                results[result].append('')
    return {
        'recur_dates' : [x.strftime('%F') for x in dates], 
        'recur_tasks' : results}
    


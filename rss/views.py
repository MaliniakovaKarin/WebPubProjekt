from django.shortcuts import render

from django.http import HttpResponse

import feedparser
from _datetime import datetime

def index(request):

    if request.GET.get("url"):

        url = request.GET["url"] #zoberie URL

        feed = feedparser.parse(url) #parsuje XML data

        entries_sort = sorted(feed.entries,key=lambda entry: datetime.strptime(entry.published, '%a, %d %b %Y %H:%M:%S %z'))
        feed['entries'] = entries_sort

        if request.GET.get('sort'):
            sort = request.GET['sort']
            if (sort == 'descending'):
                entries_sort.reverse()
                feed['entries'] = entries_sort
                return render(request, 'rss/reader.html', {   #tu sa data pošlú do reader.html, na základe toho ako ich chcem zobrazovať 
                    'feed': feed,
                    'url' : url
                })
            if (sort == 'ascending'):
                feed['entries'] = entries_sort
                return render(request, 'rss/reader.html', {
                    'feed': feed,
                    'url' : url
                })
    else:

        feed = None

    return render(request, 'rss/reader.html', {

        'feed' : feed,

    })

from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.encoding import smart_str
import youtube_dl

import random

# Create your views here.

def index(request):
    # return HttpResponse("You are viewing videodownloader index page")
    return render(request, 'videodownloader/index.html')

def downloadfile(request):
    # return HttpResponseRedirect(reverse("videodownloader:index"))
    options = {
    'outtmpl': '%(title)s-%(id)s.%(ext)s',
    'format': 'best'
    }  # save file as the YouTube ID
    with youtube_dl.YoutubeDL(options) as ydl:
        # videoFile = ydl.download([request.POST['videourl']])
        r = ydl.extract_info(request.POST['videourl'], download=False)
        videoUrl = r['url']
        fileName = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(8))
        name = "something"
        finalLink = videoUrl + "&title=" + fileName
    context = {"videoUrl":videoUrl, "filename":name, "finalLink":smart_str(finalLink)}

    return render(request, 'videodownloader/downloadfile.html', context)

    # return HttpResponse("%s was uploaded by '%s' and has %d views, %d likes, and %d dislikes and url is %s url" % (r['title'], r['uploader'], r['view_count'], r['like_count'], r['dislike_count'], r['url']))
    # return HttpResponse("url is : %s" % (r['url']))

    # response = HttpResponse(content_type='application/force-download')
    # response['Content-Disposition'] = 'attachment; filename="something"'
    # response['X-Sendfile'] = smart_str(finalLink)
    # return response

    # response = HttpResponse(content_type='application/force-download')
    # response['Content-Disposition'] = 'attachment; filename="something.mp4"'
    # return response

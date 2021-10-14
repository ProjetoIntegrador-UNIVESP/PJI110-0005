import re
from django.shortcuts import render
from django.utils.timezone import datetime
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    return render(
        request,
        'example/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
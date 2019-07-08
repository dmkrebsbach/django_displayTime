from django.shortcuts import render
from time import gmtime, strftime

def index(request):
    time = strftime("%Y-%m-%d %H:%M %p", gmtime())
    
    context = {
        "time" : time,
    }
    return render(request, 'timeDisplay/index.html', context)
# Create your views here.

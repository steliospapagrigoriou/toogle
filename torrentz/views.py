# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from toogle import torrentz_scrapper as ts

def index(request):
    return render(request,'torrentz/index.html',{})

def search(request):
    """ 
    EDW KANOUME SEARCH
    """
    data = request.POST
    print data["query"]
    link = ts.search(data["query"])
    print link
    
    print "VRES TO SITE!!!"
    return render(request,'torrentz/index.html',{})

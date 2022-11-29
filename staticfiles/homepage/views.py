from django.shortcuts import render,redirect
from hashlib import md5
from homepage.models import URL
import pyperclip as pc




# Create your views here.
def index(request):
    if request.method == "POST":
        full_url = request.POST.get('full_url')
        
        obj= URL.create(full_url)
        return render(request,"index.html",{
            'full_url': obj.full_url,
            'short_url': request.get_host() + "/"+   obj.short_url,
            
        })
        text = pc.copy('short_url')
    return render(request,'index.html')


def routeToURL(request,key):
    try:
        obj = URL.objects.get(short_url=key)
        return redirect(obj.full_url)
    except:
        obj= None
    if obj:
        pass
    return redirect(index)
    
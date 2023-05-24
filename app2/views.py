from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def app2_string(request):
    return HttpResponse('<h1>this is my app2_string</h1>')


def app2_htmlpage(request):
    return render(request,'app2_htmlpage.html')
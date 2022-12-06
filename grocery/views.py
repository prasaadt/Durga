from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.

def afternoon(request):
    return HttpResponse('<h1>Good Afternoon everybody</h1>')
def wish(request):
    date=datetime.datetime.now()
    my_dict={'insert_date': date}
    return render(request,'wish.html',context=my_dict)

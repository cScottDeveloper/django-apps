from django.http import HttpResponse
from django.shortcuts import render


# Create your views here. This is the business logic portion of the MVT
# The urls.py goes here to figure out how you want to handle the views.
def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2
    return render(request, 'result.html', {'result': res})


# method to accept client request for home page and return HttpResponse
def hello(request):
    return render(request, 'home.html', {'name': 'Chandler'})


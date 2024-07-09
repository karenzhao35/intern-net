from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request -> response (request handler)

def say_hello(request):
    # pull data, transform data, pass data to template
    return render(request, 'hello.html', {'name': 'Karen'})
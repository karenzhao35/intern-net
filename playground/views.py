from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
# request -> response (request handler)
import json

@api_view(['GET'])
def hello_view(request):
    data = {
        # Your JSON data here
        "message": "Hello, World!",
        "status": "success"
    }
    return Response(data)
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

from django.http import HttpResponse


def welcome(request):
        return HttpResponse('Hello, World!')


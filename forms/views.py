from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Order Coffee, Submit Feedback, or Go Away")
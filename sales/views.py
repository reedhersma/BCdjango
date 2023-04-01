from django.shortcuts import render
from django.http import HttpResponse
from . models import Submission, Product

def index(request):
    products = Product.objects.all()
    return HttpResponse("Order Coffee, Submit Feedback, or Go Away")
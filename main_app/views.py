from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# Create your views here.
def root(response):
    return HttpResponse("Hello World!")

def index(response):
    return HttpResponse("placeholder to later display a list of blogs")

def new(response):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(response):
    return redirect('/')

def show(response, number):
    return HttpResponse("placeholder to display blog number: " + number)

def edit(response, number):
    return HttpResponse("placeholder to edit blog " + number)

def destroy(response, number):
    return redirect('/blogs')

def json(response):
    return JsonResponse({'title': 'placeholder title', 'content': 'lorem ipsum content'})
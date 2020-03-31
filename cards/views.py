from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('<h1>Which Card</h1>')

def form(request):
    return render(request, 'cards/cardform.html')


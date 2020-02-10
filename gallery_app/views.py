from django.http import HttpResponse
from django.views.generic import CreateView
from django.shortcuts import render
from .models import Person
 

def index(request):
    return render(request, "gallery_app/index.html")

def about(request):
    return render(request, "gallery_app/about.html")

def blog(request):
    return render(request, "gallery_app/blog.html")

def portfolio(request):
    return render(request, "gallery_app/portfolio.html")

def contact(request):
    return render(request, "gallery_app/contact.html")

class PersonCreateView(CreateView):
    model = Person
    fields = ('name', 'email', 'how_known', 'comment')


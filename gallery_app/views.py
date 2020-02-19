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

def contact(request):
    return render(request, "sendemail/email.html")

def landscape(request):
    return render(request, "gallery_app/landscape.html")
def wedding(request):
    return render(request, "gallery_app/wedding.html")
def portrait(request):
    return render(request, "gallery_app/portrait.html")

# This buys you something. Connects to the shopping app. update on urls of the project
#def buy(request):
 #   return render(request, "shopping_app/shopping.html")

class PersonCreateView(CreateView):
    model = Person
    fields = ('name', 'email', 'how_known', 'comment')


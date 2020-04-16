from django.http import HttpResponse
from django.views.generic import CreateView
from django.shortcuts import render
from .models import Person
 

def gallery(request):
    return render(request, "gallery_app/index.html")

def blog(request):
    return render(request, "gallery_app/blog.html")

def contact(request):
    return render(request, "sendemail/email.html")

def wedding(request):
    return render(request, "gallery_app/wedding.html")

def featured(request):
    return render(request, "gallery_app/featured.html")

def portrait(request):
    return render(request, "gallery_app/portrait.html")

# This buys you something. Connects to the shopping app. update on urls of the project
#def buy(request):
 #   return render(request, "shopping_app/shopping.html")

class PersonCreateView(CreateView):
    model = Person
    fields = ('name', 'email', 'how_known', 'comment')


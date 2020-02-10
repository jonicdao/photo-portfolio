from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

def shoppingView(request):
    return render(request, "shopping_app/shopping.html")

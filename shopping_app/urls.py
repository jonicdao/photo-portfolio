from django.conf.urls import url
from django.urls import path, include
from .views import shoppingView

urlpatterns = [
    path('', shoppingView, name='shopping'),
]


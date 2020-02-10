from django.urls import path
from . import views
from gallery_app.views import PersonCreateView

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('add/', PersonCreateView.as_view(), name='person_add')
]
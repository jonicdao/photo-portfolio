from django.urls import path
from . import views
#from gallery_app.views import PersonCreateView
#from django.views.generic import TemplateView


urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('featured/', views.featured, name='featured'),
    path('wedding/', views.wedding, name='wedding'),
    path('portrait/', views.portrait, name='portrait'),
   # path('buy/', views.buy, name='buy'),
   # path('blog/', views.blog, name='blog'),
   # path('contact/', views.contact, name='contact'),
   # path('add/', PersonCreateView.as_view(), name='person_add'),
    # path('instagram/', TemplateView.as_view(template_name='instagram.html', extra_context={"instagram_profile_name": "josenicdao"})),
]
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static, settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sendemail/', include('sendemail.urls'), name='sendemail'),
    path('blog/', include('blog_app.urls'), name='blog'),
    path('gallery/', include('gallery_app.urls'), name='gallery'),
    path('about/', include('about.urls'), name='about'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

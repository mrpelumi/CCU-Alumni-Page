from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('news.urls')),
]

admin.site.site_header  =  "CCU Alumni Admin"  
admin.site.site_title  =  "CCU Admin Alumni site"
admin.site.index_title  =  "CCU Alumni Admin"

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
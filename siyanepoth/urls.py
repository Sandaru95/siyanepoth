from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.shortcuts import redirect

def returnToHome(request):
    return redirect('/home/')

urlpatterns = [
    path('', returnToHome),
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('publisher/', include('publisher.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
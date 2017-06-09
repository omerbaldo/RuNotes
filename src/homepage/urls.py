from django.conf.urls import include, url
from django.contrib import admin
from run_user import views 
from django.conf.urls.static import static #testing
from django.conf import settings
from django.shortcuts import render
from homepage.views import home
from homepage.views import details_1
from homepage.views import details_2
from homepage.views import details_3
from homepage.views import terms


from django.conf.urls.static import static

urlpatterns = [
	url(r'^', home,name='home'),
]

if settings.DEBUG:
    urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

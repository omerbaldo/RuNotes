"""RUNV2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from run_user import views 
from django.conf.urls.static import static #testing
from django.conf import settings
from django.shortcuts import render
from homepage.views import details_1, details_2, details_3, term
from django.conf.urls.static import static


urlpatterns = [
    # Examples:
    # url(r'^$', 'suliman_baldo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', include('homepage.urls')),

    url(r'^run_user/', include('run_user.urls')),   
    url(r'^details_1/', details_1),    
    url(r'^details_2/', details_2),   
    url(r'^details_3/', details_3),   
    url(r'^terms/', term),   
    url(r'^accounts/', include('allauth.urls')),
    #url(r'^uploads/', include('uploads.urls')),



 
] 

if settings.DEBUG:
    urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 


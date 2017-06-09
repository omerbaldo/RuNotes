from django.conf.urls import include, url
from django.contrib import admin
from run_user import views 
from django.conf.urls.static import static #testing
from django.conf import settings
from django.shortcuts import render

from django.conf.urls.static import static

from run_user.views import signup
from run_user.views import login


urlpatterns = [
    # Examples:
    # url(r'^$', 'suliman_baldo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/$', login),    
    url(r'^signup/$', signup),    
] 

if settings.DEBUG:
    urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 


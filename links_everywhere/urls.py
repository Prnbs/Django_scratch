"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from links_everywhere.views import get_my_url, get_my_tags, get_related_url, save_url

urlpatterns = [
    url(r'^getmyurl/$', get_my_url),
    url(r'^getmytags/$', get_my_tags),
    url(r'^getrelatedurl/([A-Za-z0-9]+)$', get_related_url),
    url(r'^saveurl/$', save_url)

]

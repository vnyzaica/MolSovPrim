"""firstapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url

from article.views import *
urlpatterns =(
    url(r'^1/','article.views.basic_one'),
    url(r'^2/','article.views.template_two'),
    url(r'^3/','article.views.template_three_simple'),
    url(r'^articles/all/$/','article.views.articles'),
    url(r'^articles/get/(?P<article_id>\d+)/$','article.views.article'),
)

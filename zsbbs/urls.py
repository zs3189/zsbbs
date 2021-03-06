"""zsbbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
import bbsapp.urls
import authapp.urls
import rest_framework
from django.contrib.auth import urls as auth_urls

from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'',include(bbsapp.urls)),
    url(r'^authapp/',include(authapp.urls)),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    url(r'^',include('playtogether.urls')),
    url(r'^schema/$', schema_view),

]

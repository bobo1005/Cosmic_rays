"""Data_analysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from analysis import views
from rate_angle import views as views2
from contacts import views as views3
from experimental import views as views4
from abstract import views as views5
from photo import views as views6
from rate_floor import views as views7
from rate_altitude import views as views8

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.analysis, name='home'),
    path('rate_angle', views2.rate_angle, name='rate_angle'),
    path('contacts', views3.contacts, name='contacts'),
    path('experimental_setup', views4.experimental, name='experimental'),
    path('abstract', views5.abstract, name='abstract'),
    path('photos', views6.photo, name='photo'),
    path('rate_floor', views7.rate_floor, name='rate_floor'),
    path('rate_altitude', views8.rate_altitude, name='rate_altitude'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

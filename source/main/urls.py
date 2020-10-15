"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from api_v1.views import math, get_token_view
from webapp.views import Index_View_v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index_View_v2.as_view(), name='index'),
    path('add/', math),
    path('subtract/', math),
    path('multiply/', math),
    path('divide/', math),
    path('get_token/', get_token_view)
]
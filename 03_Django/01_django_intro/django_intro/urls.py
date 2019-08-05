"""django_intro URL Configuration

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
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('introduce/', views.introduce),
    path('dinner/', views.dinner),
    path('image/', views.image),
    path('hello/<name>/<int:age>/', views.hello),
    path('master/<name>/<int:age>/', views.master),
    path('mul/<int:num1>/<int:num2>/', views.mul),
    path('circle_area/<int:rad>/', views.circle_area),
    path('template_language/', views.template_language),
]

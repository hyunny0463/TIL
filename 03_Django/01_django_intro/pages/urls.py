from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('introduce/', views.introduce),
    path('dinner/', views.dinner),
    path('image/', views.image),
    path('hello/<name>/<int:age>/', views.hello),
    path('master/<name>/<int:age>/', views.master),
    path('mul/<int:num1>/<int:num2>/', views.mul),
    path('circle_area/<int:rad>/', views.circle_area),
    path('template_language/', views.template_language),
    path('isbirth/', views.isbirth),
    path('ispal/<str:words>', views.ispal),
    path('lotto/', views.lotto),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('ping/', views.ping),
    path('pong/', views.pong),
    path('art/', views.art),
    path('result/', views.result),
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),
    path('static_example/', views.static_example),
]
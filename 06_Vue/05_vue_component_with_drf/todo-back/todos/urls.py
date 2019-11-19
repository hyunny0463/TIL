from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('todos/', views.todo_create),
    path('todos/<int:id>/', views.todo_update_delete),
    path('users/', views.user_signup),
    path('users/<int:id>/', views.user_detail),
]

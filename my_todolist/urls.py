"""my_todo_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from my_todolist import views

app_name = 'my_todolist'
urlpatterns = [
    
    path('', views.mytask, name='mytask'),
    path("delete/<int:pk>/", views.delete_task, name='delete_task'),
    path("edit/<int:pk>/", views.edit_task, name='edit_task'),
    path("update/<int:pk>/", views.update_task, name='update_task'),
    path("edit_status/<int:pk>/<str:status>", views.edit_status, name='edit_status'),
]

from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.homePage, name='homePage'),
    path("list/", views.listPage, name='listPage'),
    path("get/", views.getPage, name='getPage'),
    path("get/<str:org>", views.get, name='get')
    ]
from django.urls import path, include
from . import views

urlpatterns = [
    path("getapi/", views.first_view, name='first_view')
    ]

from django.urls import path

from Classes.campusApp import views

urlpatterns = [
    path('admin_console', views.admin_console, name="admin_console"),




]


from django.contrib import admin
from django.urls import path
from . import views
app_name='posts'
urlpatterns = [
    path("", views.to_homepage),
    path("create/", views.createpost),
    path("edit/", views.editpost),
    path("<slug:ulink>", views.showpost, name='viewpost')
    ]


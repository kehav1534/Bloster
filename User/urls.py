from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'user'
urlpatterns = [
    path("login/", views.user_login, name='login'),
    path("signup/", views.user_signup, name='signup'),
    path("profile/", views.user_profile),
    path("dashboard/", views.dashboard),
    path("logout/", views.user_logout)
]

from django.urls import include, path
from app import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from django.views.generic import TemplateView

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('register/<uuid:token>/', views.register_view, name='register_with_token')
]

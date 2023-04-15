from django.urls import path
from . import views
from django.views.generic.base import TemplateView

"""Defines URL patterns for exams"""
app_name = 'users'
urlpatterns = [
    path('register/', views.registration, name='registration'),
    path('login/', TemplateView.as_view(template_name='users/login.html'), name='login'),
]
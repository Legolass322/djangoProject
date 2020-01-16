from django.urls import path
from . import views

urlpatterns = [
    path('', views.empty, name = 'empty')
]
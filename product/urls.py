from django.urls import path

urlpatterns = [
    path('', views.empty, name = 'empty')
]
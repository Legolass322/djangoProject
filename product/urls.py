from django.urls import path
from . import views

urlpatterns = [
    path('', views.empty, name = 'empty'),
    path('/<int:product_id>/', views.get_product, name = 'get_product'),
]
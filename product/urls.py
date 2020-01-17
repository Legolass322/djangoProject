from django.urls import path
from . import views


app_name = 'product'
urlpatterns = [
    path('', views.empty, name = 'empty'),
    path('<int:product_id>/', views.get_product, name = 'get_product'),
    path('test/<int:product_id>/', views.test, name = 'test'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/order/', views.order_service, name='order_service'),
]
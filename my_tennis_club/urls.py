from django.contrib import admin
from django.urls import path
from members import views

urlpatterns = [
    path('',views.members),
    path('product', views.product)
]

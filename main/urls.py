from django.urls import include, path
from . import views
from django.views.generic import View
from rest_framework import routers

urlpatterns = [
    path('', views.ShoppingListAPIView.as_view(), name='shopping_list'),
    path('<int:id>/', views.ShoppingListItemsInstanceAPIView.as_view(), name='shopping_list_items'),
    path('<int:id>/<str:filter_val>/', views.ShoppingFilterListItemsView.as_view(), name='shopping_list_filter')
]
from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('product/', ProductListView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view())
]

from django.urls import path
from .views import ProductListView, ProductDetailView, ProductReviewsCreateView

urlpatterns = [
    path('product/', ProductListView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),
    path('review/', ProductReviewsCreateView.as_view())
]

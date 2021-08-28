from django.urls import path
from .views import ListCategory, DetailCategory

urlpatterns = [
    path('', ListCategory.as_view()),
    path('<int:pk>/', DetailCategory.as_view()),
]

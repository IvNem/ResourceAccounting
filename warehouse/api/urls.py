from django.urls import path
from .api_views import ProductDetailAPIView, TotalCostAPIView, ProductListAPIView

# установка связи между конкретным url и представлением
urlpatterns = [
    path('resources/', ProductListAPIView.as_view()),
    path('resources/<int:pk>', ProductDetailAPIView.as_view()),
    path('total_cost/', TotalCostAPIView.as_view())
]
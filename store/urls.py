from django.urls import path
from store import views

urlpatterns = [
    path('product/', views.ProductListCreateAPIView.as_view()),
    path('product/<str:pk>/', views.ProductRetrieveUpdateDeleteAPIView.as_view()),

    path('category/', views.CategoryListCreateAPIView.as_view()),
    path('category/<str:pk>/', views.CategoryRetrieveUpdateDeleteAPIView.as_view()),

    path('shop/', views.ShopListCreateAPIView.as_view()),
    path('shop/<str:pk>/', views.ShopRetrieveUpdateDeleteAPIView.as_view()),

]


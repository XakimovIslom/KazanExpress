from rest_framework import filters
from rest_framework import generics
from rest_framework import permissions

from store.models import Category, Shop, Product
from store.permissions import IsShopAdminOrReadOnly, IsCategoryAdminOrReadOnly, IsProductAdminOrReadOnly
from store.serializers import CategorySerializer, ShopSerializer, ProductSerializer


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.select_related('parent').all()
    serializer_class = CategorySerializer
    # permission_classes = (IsCategoryAdminOrReadOnly,)


class CategoryRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (IsCategoryAdminOrReadOnly,)


class ShopListCreateAPIView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    # permission_classes = (IsShopAdminOrReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class ShopRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    # permission_classes = (IsShopAdminOrReadOnly,)


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.select_related('shop', 'category').prefetch_related('photos').all()
    serializer_class = ProductSerializer
    # permission_classes = (IsProductAdminOrReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'title']


class ProductRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = (IsProductAdminOrReadOnly,)

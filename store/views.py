from rest_framework import filters
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.views import APIView

from store.models import Category, Shop, Product
from store.permissions import IsShopAdminOrReadOnly, IsCategoryAdminOrReadOnly, IsProductAdminOrReadOnly
from store.serializers import CategorySerializer, ShopSerializer, ProductSerializer
from store.throttling import CustomHourlyThrottle
from datetime import datetime, time


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.select_related('parent').all()
    serializer_class = CategorySerializer
    # permission_classes = (IsCategoryAdminOrReadOnly,)


class CategoryRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (IsCategoryAdminOrReadOnly,)


# class ShopListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Shop.objects.all()
#     serializer_class = ShopSerializer
#     # permission_classes = (IsShopAdminOrReadOnly,)
#     throttle_classes = (CustomHourlyThrottle,)
#
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['title']


class ShopListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        shop = Shop.objects.all().values()
        current_time = datetime.now().time()

        start_time = time(18, 00)
        end_time = time(20, 00)

        if start_time <= current_time < end_time:
            return Response({'shop': list(shop)})
        return Response({"message": f"API is available between {start_time} and {end_time}"})


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

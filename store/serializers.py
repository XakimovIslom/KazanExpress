from rest_framework import serializers
from store.models import Category, Shop, Product, Photo


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'parent',
            'description',
            'created_at',
            'updated_at'
        )


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = (
            'id',
            'title',
            'description',
            'image',
            'created_at',
            'updated_at'
        )
        read_only_fields = ['id']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('product', 'image')


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(source='category.title')
    photos = PhotoSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'photos',
            'main_image',
            'uploaded_images',
            'category',
            'description',
            'amount',
            'price',
            'is_active',
            'created_at',
            'updated_at'
        )

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images')
        product = Product.objects.create(**validated_data)
        for image in uploaded_images:
            new_product_image = Photo.objects.create(product=product, image=image)
        return product

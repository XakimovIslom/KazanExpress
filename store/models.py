import uuid

from django.db import models

from config.settings.base import AUTH_USER_MODEL
from store.utils import BaseModel


class Role(BaseModel):
    title = models.CharField(max_length=128)
    role = models.ManyToManyField(AUTH_USER_MODEL, related_name='roles')

    def __str__(self):
        return self.title


class Category(BaseModel):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=256)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='parents')
    description = models.TextField()

    def __str__(self):
        return self.title


class Shop(BaseModel):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to='store/', null=True, blank=True)

    def __str__(self):
        return self.title


class Product(BaseModel):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=256)
    main_image = models.ImageField(upload_to='product', null=True, blank=True)

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='shops', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories', null=True, blank=True)

    description = models.TextField()
    amount = models.IntegerField()
    price = models.FloatField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Photo(BaseModel):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    image = models.ImageField(upload_to="photos")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="photos")
    is_main = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_main:
            self.product.main_image = self.image
            self.product.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product.title

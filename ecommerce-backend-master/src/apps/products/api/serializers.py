from rest_framework import serializers

from ..models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Category
        fields = ("id", "name")


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "price",
            "quantity",
            "featured",
            "description",
            "picture",
            "slug",
        )
        lookup_field = "slug"

from rest_framework import serializers
from .models import Category, CategorySample

from ..utils import convert_to_snake_case


class CategorySerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        new_data = {}
        for key, value in data.items():
            new_key = convert_to_snake_case(key)
            new_data[new_key] = value
        return super().to_internal_value(new_data)

    class Meta:
        model = Category
        fields = "__all__"
        extra_kwargs = {"category_name": {"required": False}}


class CategorySampleSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        new_data = {}
        for key, value in data.items():
            new_key = convert_to_snake_case(key)
            new_data[new_key] = value
        return super().to_internal_value(new_data)

    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = CategorySample
        fields = ["category_id"]

from rest_framework import serializers
from .models import Subcategory, SubcategorySample

from ...utils import convert_to_snake_case


class SubcategorySerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        new_data = {}
        for key, value in data.items():
            new_key = convert_to_snake_case(key)
            new_data[new_key] = value
        return super().to_internal_value(new_data)

    class Meta:
        model = Subcategory
        fields = "__all__"
        extra_kwargs = {"subcategory_name": {"required": False}}


class SubcategorySampleSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        new_data = {}
        for key, value in data.items():
            new_key = convert_to_snake_case(key)
            new_data[new_key] = value
        return super().to_internal_value(new_data)

    subcategory_id = serializers.PrimaryKeyRelatedField(
        queryset=Subcategory.objects.all()
    )

    class Meta:
        model = SubcategorySample
        fields = ["subcategory_id"]

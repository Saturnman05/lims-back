from rest_framework import serializers
from .models import Ingredient, SampleIngredient

from ..utils import convert_to_snake_case


class IngredientSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        new_data = {}
        for key, value in data.items():
            new_key = convert_to_snake_case(key)
            new_data[new_key] = value
        return super().to_internal_value(new_data)

    class Meta:
        model = Ingredient
        fields = "__all__"
        extra_kwargs = {"ingredient_name": {"required": False}}


class SampleIngredientSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        new_data = {}
        for key, value in data.items():
            new_key = convert_to_snake_case(key)
            new_data[new_key] = value
        return super().to_internal_value(new_data)

    ingredient_id = serializers.PrimaryKeyRelatedField(
        queryset=Ingredient.objects.all()
    )

    class Meta:
        model = SampleIngredient
        fields = ["ingredient_id"]

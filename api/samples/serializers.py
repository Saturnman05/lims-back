from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Sample

from ..allergens.serializers import AllergenSerializer, AllergenSampleSerializer
from ..categorys.serializers import CategorySerializer, CategorySampleSerializer
from ..ingredients.serializers import IngredientSerializer, SampleIngredientSerializer

from ..allergens.models import AllergenSample
from ..categorys.models import CategorySample
from ..ingredients.models import SampleIngredient

from ..utils import convert_to_snake_case


class SampleSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        new_data = {}
        for key, value in data.items():
            new_key = convert_to_snake_case(key)
            new_data[new_key] = value
        return super().to_internal_value(new_data)

    allergens = AllergenSampleSerializer(many=True)
    categorys = CategorySampleSerializer(many=True)
    ingredients = SampleIngredientSerializer(many=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all()
    )

    class Meta:
        model = Sample
        fields = [
            "sample_id",
            "comercial_name",
            "product_brand",
            "batch_code",
            "production_date",
            "expiration_date",
            "quantity_units",
            "is_rejected",
            "origin_country",
            "collection_date",
            "temperature",
            "special_conditions",
            "user_id",
            "allergens",
            "categorys",
            "ingredients",
        ]

    def create(self, validated_data):
        print(f"validated data: {validated_data}\n\n")
        allergens_data = validated_data.pop("allergens")
        categorys_data = validated_data.pop("categorys")
        ingredients_data = validated_data.pop("ingredients")

        sample = Sample.objects.create(**validated_data)

        for allergen_data in allergens_data:
            AllergenSample.objects.create(
                Sample=sample, Allergen=allergen_data["allergen_id"]
            )

        for category_data in categorys_data:
            CategorySample.objects.create(
                Sample=sample, Category=category_data["category_id"]
            )

        for ingredient_data in ingredients_data:
            SampleIngredient.objects.create(
                Sample=sample, Ingredient=ingredient_data["ingredient_id"]
            )

        return sample

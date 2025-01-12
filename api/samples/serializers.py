from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Sample

from ..allergens.serializers import AllergenSampleSerializer
from ..categorys.serializers import CategorySampleSerializer
from ..ingredients.serializers import SampleIngredientSerializer

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
            "is_request",
        ]

    def create(self, validated_data):
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

    def update(self, validated_data):
        # Obtener los datos actuales
        before_sample = Sample.objects.get(pk=validated_data["sample_id"])
        before_allergens_data = before_sample.allergens
        before_categorys_data = before_sample.categorys
        before_ingredients_data = before_sample.ingredients

        # Datos para actualizar
        allergens_data = validated_data.pop("allergens")
        categorys_data = validated_data.pop("categorys")
        ingredients_data = validated_data.pop("ingredients")

        sample = Sample.objects.update(**validated_data)

        # UPDATE allergens
        before_allergen_ids = set(
            before_allergens_data.values_list("allergen_id", flat=True)
        )
        allergen_ids = set([allergen["allergen_id"] for allergen in allergens_data])
        new_allergen_ids = []
        for id in before_allergen_ids:
            if not id in allergen_ids:
                AllergenSample.objects.filter(
                    Sample=before_sample, Allergen=id
                ).delete()
            else:
                new_allergen_ids.append(id)

        for id in set(allergen_ids + new_allergen_ids):
            AllergenSample.objects.create(Sample=sample, Allergen=id)

        # UPDATE categorys
        before_category_ids = set(
            before_categorys_data.values_list("category_id", flat=True)
        )
        category_ids = set([category["category_id"] for category in categorys_data])
        new_category_ids = []
        for id in before_category_ids:
            if not id in category_ids:
                CategorySample.objects.filter(
                    Sample=before_sample, Category=id
                ).delete()
            else:
                new_category_ids.append(id)

        for id in set(category_ids + new_category_ids):
            CategorySample.objects.create(Sample=sample, Category=id)

        # TODO: UPDATE ingredients
        before_ingredient_ids = set(
            before_ingredients_data.values_list("ingredient_id", flat=True)
        )
        ingredient_ids = set(
            [ingredient["ingredient_id"] for ingredient in ingredients_data]
        )
        new_ingredient_ids = []
        for id in before_ingredient_ids:
            if not id in ingredient_ids:
                SampleIngredient.objects.filter(
                    Sample=before_sample, Ingredient=id
                ).delete()
            else:
                new_ingredient_ids.append(id)
        for ingredient_data in ingredients_data:
            SampleIngredient.objects.create(
                Sample=sample, Ingredient=ingredient_data["ingredient_id"]
            )

        return sample

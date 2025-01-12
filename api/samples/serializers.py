from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Sample

from .allergens.serializers import AllergenSampleSerializer
from .categorys.serializers import CategorySampleSerializer
from .ingredients.serializers import SampleIngredientSerializer

from .allergens.models import AllergenSample
from .categorys.models import CategorySample
from .ingredients.models import SampleIngredient

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

    def update(self, instance, validated_data):
        # Obtener los datos actuales
        before_allergens_data = instance.allergens.all()
        before_categorys_data = instance.categorys.all()
        before_ingredients_data = instance.ingredients.all()

        # Datos para actualizar
        allergens_data = validated_data.pop("allergens")
        categorys_data = validated_data.pop("categorys")
        ingredients_data = validated_data.pop("ingredients")

        # Actualizar el Sample
        instance = super().update(instance, validated_data)

        # UPDATE allergens
        self.update_relations(
            instance,
            before_allergens_data,
            allergens_data,
            "allergen_id",
            AllergenSample,
        )

        # UPDATE categorys
        self.update_relations(
            instance,
            before_categorys_data,
            categorys_data,
            "category_id",
            CategorySample,
        )

        # UPDATE ingredients
        self.update_relations(
            instance,
            before_ingredients_data,
            ingredients_data,
            "ingredient_id",
            SampleIngredient,
        )

        return instance

    def update_relations(
        self, instance, before_relaions_data, relations_data, id_field, relation_model
    ):
        before_relation_ids = set(before_relaions_data.values_list(id_field, flat=True))
        relation_ids = set([relation[id_field] for relation in relations_data])

        # Eliminar relaciones que ya no existen (corregido)
        for relation_id in before_relation_ids - relation_ids:
            relation_model.objects.filter(
                Sample=instance, **{id_field.capitalize(): relation_id}
            ).delete()

        for relation_id in relation_ids - before_relation_ids:
            relation_model.objects.create(
                Sample=instance, **{id_field.capitalize(): relation_id.pk}
            )

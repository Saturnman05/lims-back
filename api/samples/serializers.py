from django.contrib.auth import get_user_model

from rest_framework import serializers, status
from rest_framework.response import Response

from .models import Sample

from .categorys.serializers import CategorySampleSerializer
from .subcategorys.serializers import SubcategorySampleSerializer
from .files.serializers import FileSerializer

from .categorys.models import CategorySample
from .subcategorys.models import SubcategorySample
from .files.models import File

from ..utils import convert_to_snake_case


class SampleCreateSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        new_data = {}
        for key, value in data.items():
            new_key = convert_to_snake_case(key)
            new_data[new_key] = value
        return super().to_internal_value(new_data)

    categorys = CategorySampleSerializer(many=True)
    subcategorys = SubcategorySampleSerializer(many=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all()
    )
    file_id = serializers.PrimaryKeyRelatedField(queryset=File.objects.all())
    files = FileSerializer(many=True)

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
            "categorys",
            "subcategorys",
            "is_request",
            "user_id",
            "file_id",
            "files",
        ]
        extra_kwargs = {
            "comercial_name": {"required": True},
            "product_brand": {"required": True},
            "batch_code": {"required": True},
            "production_date": {"required": True},
            "expiration_date": {"required": True},
            "quantity_units": {"required": True},
            "is_rejected": {"required": False},
            "origin_country": {"required": True},
            "collection_date": {"required": False},
            "temperature": {"required": False},
            "special_conditions": {"required": False},
            "user_id": {"required": False},
            "categorys": {"required": True},
            "subcategorys": {"required": True},
            "is_request": {"required": False},
            "file_id": {"required": False},
        }

    def create(self, validated_data):
        print(validated_data)
        user_id = self.context["request"].user
        validated_data.pop("user_id")
        validated_data.pop("file_id")

        categorys_data = validated_data.pop("categorys")
        subcategorys_data = validated_data.pop("subcategorys")
        files_data = validated_data.pop("files", None)
        file_instance = None
        if files_data:
            file_serializer = FileSerializer(data=files_data)
            file_serializer.is_valid(raise_exception=True)
            file_instance = file_serializer.save()

        sample = Sample.objects.create(
            user_id=user_id, file_id=file_instance, **validated_data
        )

        for category_data in categorys_data:
            CategorySample.objects.create(
                Sample=sample, Category=category_data["category_id"]
            )

        for subcategory_data in subcategorys_data:
            SubcategorySample.objects.create(
                Sample=sample, Subcategory=subcategory_data["subcategory_id"]
            )
        sample.files = []
        return sample


class SampleSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        new_data = {}
        for key, value in data.items():
            new_key = convert_to_snake_case(key)
            new_data[new_key] = value
        return super().to_internal_value(new_data)

    categorys = CategorySampleSerializer(many=True)
    subcategorys = SubcategorySampleSerializer(many=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all()
    )
    file_id = serializers.PrimaryKeyRelatedField(queryset=File.objects.all())

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
            "categorys",
            "subcategorys",
            "is_request",
            "user_id",
            "file_id",
        ]
        extra_kwargs = {
            "comercial_name": {"required": True},
            "product_brand": {"required": True},
            "batch_code": {"required": True},
            "production_date": {"required": True},
            "expiration_date": {"required": True},
            "quantity_units": {"required": True},
            "is_rejected": {"required": False},
            "origin_country": {"required": True},
            "collection_date": {"required": False},
            "temperature": {"required": False},
            "special_conditions": {"required": False},
            "user_id": {"required": False},
            "categorys": {"required": True},
            "subcategorys": {"required": True},
            "is_request": {"required": False},
            "file_id": {"required": False},
        }

    def update(self, instance, validated_data):
        # Obtener los datos actuales
        before_categorys_data = instance.categorys.all()
        before_subcategorys_data = instance.subcategorys.all()

        # Datos para actualizar
        categorys_data = validated_data.pop("categorys")
        subcategorys_data = validated_data.pop("subcategorys")

        # Actualizar el Sample
        instance = super().update(instance, validated_data)

        # UPDATE categorys
        self.update_relations(
            instance,
            before_categorys_data,
            categorys_data,
            "category_id",
            CategorySample,
        )

        self.update_relations(
            instance,
            before_subcategorys_data,
            subcategorys_data,
            "subcategory_id",
            SubcategorySample,
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

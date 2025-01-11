from rest_framework import serializers
from .models import Allergens

from ..utils import convert_to_snake_case


class AllergenSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        new_data = {}
        for key, value in data.items():
            new_key = convert_to_snake_case(key)
            new_data[new_key] = value
        return super().to_internal_value(new_data)

    class Meta:
        model = Allergens
        fields = "__all__"

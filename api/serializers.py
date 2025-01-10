from django.contrib.auth.hashers import make_password

from rest_framework import serializers

from .models import CustomUser  # Importa tu modelo personalizado
from .utils import convert_to_snake_case


class UserSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        new_data = {}
        for key, value in data.items():
            new_key = convert_to_snake_case(key)
            new_data[new_key] = value
        return super().to_internal_value(new_data)

    class Meta:
        model = CustomUser  # Usa tu modelo personalizado
        fields = "__all__"  # O especifica los campos que necesitas
        extra_kwargs = {"Password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.password = make_password(password)
        instance.save()
        return instance

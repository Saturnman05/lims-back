from rest_framework import serializers
from .models import User  # Importa tu modelo personalizado
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Usa tu modelo personalizado
        fields = "__all__"  # O especifica los campos que necesitas
        extra_kwargs = {"Password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("Password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.Password = make_password(password)
        instance.save()
        return instance

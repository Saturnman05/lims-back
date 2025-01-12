from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
)

from .models import Ingredient
from .serializers import IngredientSerializer


class IngredientCreate(CreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientsList(ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientDetail(RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

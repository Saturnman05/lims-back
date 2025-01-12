from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
)

from .models import Category
from .serializers import CategorySerializer


class CategoryCreate(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategorysList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

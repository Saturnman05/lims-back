from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Subcategory
from .serializers import SubcategorySerializer


class SubcategorysListCreate(ListCreateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class SubcategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

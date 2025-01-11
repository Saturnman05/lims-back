from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
)

from .models import Allergens
from .serializers import AllergenSerializer


class AllergenCreate(CreateAPIView):
    queryset = Allergens.objects.all()
    serializer_class = AllergenSerializer


class AllergensList(ListAPIView):
    queryset = Allergens.objects.all()
    serializer_class = AllergenSerializer


class AllergenDetail(RetrieveUpdateDestroyAPIView):
    queryset = Allergens.objects.all()
    serializer_class = AllergenSerializer

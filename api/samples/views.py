from rest_framework import generics
from .serializers import SampleSerializer
from .models import Sample


class SampleListCreate(generics.ListCreateAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer

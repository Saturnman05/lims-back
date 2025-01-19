from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import SampleSerializer
from .models import Sample


class SampleListCreate(generics.ListCreateAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


class SampleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer

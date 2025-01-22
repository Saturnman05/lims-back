from django.http import JsonResponse
from django.db import connection

from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import SampleCreateSerializer, SampleSerializer
from .models import Sample


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def sample_update(request):
    with connection.cursor() as cursor:
        cursor.execute(
            "EXEC spUpdateSampleAndFiles"
            + "@SampleId = %s,"
            + "@ComercialName = %s,"
            + "@ProductBrand = %s,"
            + "@BatchCode = %s,"
            + "@ProductionDate = %s,"
            + "@ExpirationDate = %s,"
            + "@QuantityUnits = %s,"
            + "@IsRejected = %s,"
            + "@OriginCountry = %s,"
            + "@CollectionDate = %s,"
            + "@Temperature = %s,"
            + "@SpecialConditions = %s,"
            + "@UserId = %s,"
            + "@IsRequest = %s,"
            + "@Files = %s",
            [
                request.data.get("sampleId"),
                request.data.get("comercialName"),
                request.data.get("productBrand"),
                request.data.get("batchCode"),
                request.data.get("productionDate"),
                request.data.get("expirationDate"),
                request.data.get("quantityUnits"),
                request.data.get("isRejected"),
                request.data.get("originCountry"),
                request.data.get("collectionDate"),
                request.data.get("temperature"),
                request.data.get("specialConditions"),
                request.data.get("userId"),
                request.data.get("isRequest"),
                request.data.get("files"),
            ],
        )
        cursor.nextset()
        cursor.nextset()

        rows = cursor.fetchall()
    data = [
        {
            "SampleId": row[0],
            "ComercialName": row[1],
            "ProductBrand": row[2],
            "BatchCode": row[3],
            "ProductionDate": row[4],
            "ExpirationDate": row[5],
            "QuantityUnits": row[6],
            "IsRejected": row[7],
            "OriginCountry": row[8],
            "CollectionDate": row[9],
            "Temperature": row[10],
            "SpecialConditions": row[11],
            "UserId": row[12],
            "IsRequest": row[13],
            "FileId": row[14],
        }
        for row in rows
    ][0]
    return JsonResponse(data, safe=False)


class SampleCreate(generics.CreateAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleCreateSerializer


class SampleList(generics.ListAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


class SampleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer

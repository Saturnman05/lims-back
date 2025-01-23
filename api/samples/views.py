import traceback
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

@api_view(["GET", "POST", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def sample_assignment(request, sample_id=None):
    """
    Handle Sample Assignment operations:
    GET: Retrieve assignment
    POST: Create new assignment
    PUT: Update assignment
    DELETE: Delete assignment
    """
    try:
        if request.method == "GET":
            if sample_id is None:
                return JsonResponse(
                    {"error": "SampleId is required"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            try:
                with connection.cursor() as cursor:
                    # Use direct SQL instead of stored procedure to debug
                    cursor.execute(
                        "SELECT * FROM Assignment WHERE SampleId = %s",
                        [sample_id]
                    )
                    rows = cursor.fetchall()
                
                if not rows:
                    return JsonResponse(
                        {"message": "No assignment found"},
                        status=status.HTTP_404_NOT_FOUND
                    )
                
                data = [
                    {
                        "assignment_id": row[0],
                        "assignment_date": row[1],
                        "sample_id": row[2],
                        "analyst_id": row[3],
                        "manager_id": row[4],
                    }
                    for row in rows
                ]
                return JsonResponse(data[0] if data else {}, safe=False)
            
            except Exception as db_error:
                return JsonResponse(
                    {
                        "error": str(db_error),
                        "traceback": traceback.format_exc()
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        
        elif request.method == "POST":
            # Create new assignment
            sample_id = request.data.get('sampleId')
            analyst_id = request.data.get('analystId')
            manager_id = request.data.get('managerId')
            
            if not all([sample_id, analyst_id, manager_id]):
                return JsonResponse(
                    {"error": "SampleId, AnalystId, and ManagerId are required"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            with connection.cursor() as cursor:
                cursor.execute(
                    "EXEC ManageSampleAssignment @SampleId=?, @AnalystId=?, @ManagerId=?, @Operation=?",
                    [sample_id, analyst_id, manager_id, 4]
                )
            
            return JsonResponse(
                {"message": "Assignment created successfully"},
                status=status.HTTP_201_CREATED
            )
        
        elif request.method == "PUT":
            # Update existing assignment
            if sample_id is None:
                sample_id = request.data.get('sampleId')
            
            analyst_id = request.data.get('analystId')
            manager_id = request.data.get('managerId')
            
            if not all([sample_id, analyst_id, manager_id]):
                return JsonResponse(
                    {"error": "SampleId, AnalystId, and ManagerId are required"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            with connection.cursor() as cursor:
                cursor.execute(
                    "EXEC ManageSampleAssignment @SampleId=?, @AnalystId=?, @ManagerId=?, @Operation=?",
                    [sample_id, analyst_id, manager_id, 2]
                )
            
            return JsonResponse(
                {"message": "Assignment updated successfully"},
                status=status.HTTP_200_OK
            )
        
        elif request.method == "DELETE":
            # Delete assignment
            if sample_id is None:
                sample_id = request.data.get('sampleId')
            
            if sample_id is None:
                return JsonResponse(
                    {"error": "SampleId is required"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            with connection.cursor() as cursor:
                cursor.execute(
                    "EXEC ManageSampleAssignment @SampleId=?, @AnalystId=NULL, @ManagerId=NULL, @Operation=?",
                    [sample_id, 3]
                )
            
            return JsonResponse(
                {"message": "Assignment deleted successfully"},
                status=status.HTTP_200_OK
            )
    
    except Exception as e:
        return JsonResponse(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

class SampleCreate(generics.CreateAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleCreateSerializer


class SampleList(generics.ListAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


class SampleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer

from django.http import JsonResponse
from django.db import connection

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(["GET", "POST", "PUT"])
@permission_classes([IsAuthenticated])
def bulletin(request):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC spBulletin @BulletinId=null, @IsPrivate=null, @SampleId=null, @EmployeeId=null, @Procedure=1"
            )
            rows = cursor.fetchall()
        data = [
            {
                "bulletin_id": row[0],
                "issuance_date": row[1],
                "is_private": row[2],
                "sample_id": row[3],
                "employee_id": row[4],
            }
            for row in rows
        ]
        return JsonResponse(data, safe=False)
    elif request.method == "POST":
        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC spBulletin @BulletinId=null, @IsPrivate=%s, @SampleId=%s, @EmployeeId=%s, @Procedure=2",
                [
                    request.data.get("isPrivate"),
                    request.data.get("sampleId"),
                    request.data.get("employeeId"),
                ],
            )

        return JsonResponse({"message": "Se creo el buletin exitosamente"})
    elif request.method == "PUT":
        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC spBulletin @BulletinId=%s, @IsPrivate=%s, @SampleId=%s, @EmployeeId=%s, @Procedure=3",
                [
                    request.data.get("bulletinId"),
                    request.data.get("isPrivate"),
                    request.data.get("sampleId"),
                    request.data.get("employeeId"),
                ],
            )
            cursor.nextset()
            rows = cursor.fetchall()
        data = [
            {
                "bulletin_id": row[0],
                "issuance_date": row[1],
                "is_private": row[2],
                "sample_id": row[3],
                "employee_id": row[4],
            }
            for row in rows
        ]
        return JsonResponse(data, safe=False)


@api_view(["GET", "DELETE"])
@permission_classes([IsAuthenticated])
def bulletin_detail(request, bulletin_id: int):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC spBulletin @BulletinId=%s, @IsPrivate=null, @SampleId=null, @EmployeeId=null, @Procedure=1",
                [bulletin_id],
            )
            rows = cursor.fetchall()
        data = [
            {
                "bulletin_id": row[0],
                "issuance_date": row[1],
                "is_private": row[2],
                "sample_id": row[3],
                "employee_id": row[4],
            }
            for row in rows
        ]

        if len(data) == 0:
            return JsonResponse(data, safe=False)
        return JsonResponse(data[0], safe=False)
    if request.method == "DELETE":
        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC spBulletin @BulletinId=%s, @IsPrivate=null, @SampleId=null, @EmployeeId=null, @Procedure=4",
                [bulletin_id],
            )

        return JsonResponse({"message": "Se elimino el buletin exitosamente"})

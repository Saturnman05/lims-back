from django.http import JsonResponse
from django.db import connection

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(["GET", "POST", "PUT"])
@permission_classes([IsAuthenticated])
def role_list(request):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC spRoles @RoleId=%s, @RoleName=%s, @RoleDescription=%s, @Procedure=1",
                [None, None, None],
            )
            rows = cursor.fetchall()

        data = [
            {"role_id": row[0], "role_name": row[1], "role_description": row[2]}
            for row in rows
        ]

        return (
            JsonResponse(data[0], safe=False)
            if len(data) == 1
            else JsonResponse(data, safe=False)
        )
    elif request.method == "POST":
        role_name = request.data.get("roleName")
        role_desc = request.data.get("roleDescription")

        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC spRoles @RoleId=0, @RoleName=%s, @RoleDescription=%s, @Procedure=2",
                [role_name, role_desc],
            )
        return JsonResponse({"message": "Se creó el rol correctamente"})
    elif request.method == "PUT":
        role_id = request.data.get("roleId")
        role_name = request.data.get("roleName")
        role_desc = request.data.get("roleDescription")

        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC spRoles @RoleId=%s, @RoleName=%s, @RoleDescription=%s, @Procedure=3",
                [role_id, role_name, role_desc],
            )
            cursor.nextset()
            rows = cursor.fetchall()

        data = [
            {"role_id": row[0], "role_name": row[1], "role_description": row[2]}
            for row in rows
        ][0]
        return JsonResponse(data, safe=False)


@api_view(["GET", "DELETE"])
@permission_classes([IsAuthenticated])
def role_delete(request, role_id):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC spRoles @RoleId=%s, @RoleName=null, @RoleDescription=null, @Procedure=1",
                [role_id],
            )
            rows = cursor.fetchall()
            try:
                data = [
                    {"role_id": row[0], "role_name": row[1], "role_description": row[2]}
                    for row in rows
                ][0]
            except:
                return JsonResponse(
                    {"message": "Error al procesar los datos"}, status=500
                )
        return JsonResponse(data, safe=False)
    elif request.method == "DELETE":
        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC spRoles @RoleId=%s, @RoleName=null, @RoleDescription=null, @Procedure=4",
                [role_id],
            )
        return JsonResponse({"message": f"Se eleminó el rol {role_id} exitosamente"})


@api_view(["GET", "POST", "PUT"])
@permission_classes([IsAuthenticated])
def user_role(request, user_id=None):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC spEmployeeRoles @NewRoleId=null, @RoleId=null, @EmployeeId=%s, @Procedure=1",
                [user_id],
            )
            rows = cursor.fetchall()
        data = [
            {
                "role_id": row[0],
                "role_name": row[1],
                "role_description": row[2],
                "user_id": row[3],
            }
            for row in rows
        ]
        return JsonResponse(data, safe=False)
    elif request.method == "POST":
        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC spEmployeeRoles @NewRoleId=null, @RoleId=%s, @EmployeeId=%s, @Procedure=2",
                [request.data.get("roleId"), request.data.get("userId")],
            )
        return JsonResponse({"message": "Se le añadió un rol al usuario exitosamente"})
    elif request.method == "PUT":
        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC spEmployeeRoles @NewRoleId=%s, @RoleId=%s, @EmployeeId=%s, @Procedure=3",
                [
                    request.data.get("newRoleId"),
                    request.data.get("roleId"),
                    request.data.get("userId"),
                ],
            )
        return JsonResponse({"message": "Se actualizó el rol del usuario exitosamente"})

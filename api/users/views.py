from django.http import JsonResponse
from django.db import connection

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, CreateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework_simplejwt.authentication import JWTAuthentication

from drf_spectacular.utils import extend_schema

from .models import User
from .serializers import UserSerializer
from ..utils import convert_to_snake_case


class CreatUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@extend_schema(responses=UserSerializer)
class UserDetailView(GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = request.user
            serializer = UserSerializer(user)
            data = {
                convert_to_snake_case(key): value
                for key, value in serializer.data.items()
            }
            return Response({"user": data})
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_role(request):
    user_id = request.user.user_id
    with connection.cursor() as cursor:
        cursor.execute(
            "EXEC spEmployeeRoles @NewRoleId=null, @RoleId=null, @EmployeeId=%s, @Procedure=1",
            [user_id],
        )
        rows = cursor.fetchall()

    if len(rows) == 0:
        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC spEmployeeRoles @NewRoleId=null, @RoleId=null, @EmployeeId=%s, @Procedure=4",
                [user_id],
            )
            rows = cursor.fetchall()

    data = [
        {
            "role_id": row[0],
            "role_name": row[1],
            "role_description": row[2],
            "user_id": row[3],
            "is_master": row[4],
        }
        for row in rows
    ]
    return JsonResponse(data, safe=False)

from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import CustomUser
from .serializers import UserSerializer
from .utils import convert_to_snake_case


class CreatUserView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


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


class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {"message": "Hello World"}
        return Response(content)

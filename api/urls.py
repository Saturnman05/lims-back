from django.urls import path
from .views import UserListView, CreatUserView, Home

urlpatterns = [
    path("users/register/", CreatUserView.as_view(), name="register"),
    # path("users/login/", CustomAuthToken.as_view(), name="login"),
    path("users/", UserListView.as_view(), name="user-list"),
    # Test endpoint
    path("", Home.as_view(), name="home"),
]

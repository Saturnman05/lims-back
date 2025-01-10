from django.urls import path
from .views import UserListView, CreatUserView, Home, UserDetailView

urlpatterns = [
    path("users/register/", CreatUserView.as_view(), name="register"),
    path("users/details/", UserDetailView.as_view(), name="user-details"),
    path("users/", UserListView.as_view(), name="user-list"),
    # Test endpoint
    path("", Home.as_view(), name="home"),
]

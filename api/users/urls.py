from django.urls import path
from .views import UserListView, CreatUserView, UserDetailView, get_user_role

urlpatterns = [
    path("register/", CreatUserView.as_view(), name="register"),
    path("details/", UserDetailView.as_view(), name="user-details"),
    path("role/", get_user_role),
    path("", UserListView.as_view(), name="user-list"),
]

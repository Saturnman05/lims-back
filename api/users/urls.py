from django.urls import path
from .views import UserListView, CreatUserView, UserDetailView

urlpatterns = [
    path("register/", CreatUserView.as_view(), name="register"),
    path("details/", UserDetailView.as_view(), name="user-details"),
    path("", UserListView.as_view(), name="user-list"),
]

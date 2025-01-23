from django.urls import path
from .views import (
    UserListView,
    CreatUserView,
    UserDetailView,
    get_user_role,
    filtered_get,
)

urlpatterns = [
    path("register/", CreatUserView.as_view(), name="register"),
    path("details/", UserDetailView.as_view(), name="user-details"),
    path("role/", get_user_role),
    path("filter/<int:role_id>/", filtered_get),
    path("filter/is-active/<int:active>/", filtered_get),
    path("filter/<int:role_id>/<int:active>/", filtered_get),
    path("", UserListView.as_view(), name="user-list"),
]

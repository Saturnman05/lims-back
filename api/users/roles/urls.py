from django.urls import path

from .views import role_list, role_detail, user_role

urlpatterns = [
    path("<int:role_id>/", role_detail),
    path("", role_list),
    path("user-role/<int:user_id>/", user_role),
    path("user-role/", user_role),
]

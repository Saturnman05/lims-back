from django.urls import path

from .views import role_list, role_delete, user_role

urlpatterns = [
    path("<int:role_id>/", role_delete),
    path("user-role/<int:user_id>/", user_role),
    path("user-role/", user_role),
    path("", role_list),
]

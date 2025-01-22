from django.urls import path

from .views import role_list, role_delete

urlpatterns = [
    path("", role_list),
    path("<int:role_id>/", role_delete),
]

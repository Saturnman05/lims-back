from django.urls import path

from .views import bulletin, bulletin_detail

urlpatterns = [
    path("", bulletin),
    path("<int:bulletin_id>/", bulletin_detail),
]

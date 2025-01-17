from django.urls import path

from .views import FileDetail, FileListCreate

urlpatterns = [
    path("<int:pk>/", FileDetail.as_view()),
    path("", FileListCreate.as_view()),
]

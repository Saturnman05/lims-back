from django.urls import path

from .views import CategoryCreate, CategoryDetail, CategorysList

urlpatterns = [
    path("create/", CategoryCreate.as_view()),
    path("<int:pk>/", CategoryDetail.as_view()),
    path("", CategorysList.as_view()),
]

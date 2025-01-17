from django.urls import path

from .views import SubcategoryDetail, SubcategorysListCreate

urlpatterns = [
    path("<int:pk>/", SubcategoryDetail.as_view()),
    path("", SubcategorysListCreate.as_view()),
]

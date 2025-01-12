from django.urls import path

from .views import IngredientCreate, IngredientDetail, IngredientsList

urlpatterns = [
    path("create/", IngredientCreate.as_view()),
    path("<int:pk>/", IngredientDetail.as_view()),
    path("", IngredientsList.as_view()),
]

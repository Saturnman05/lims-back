from django.urls import path

from .views import AllergenCreate, AllergensList, AllergenDetail

urlpatterns = [
    path("", AllergensList.as_view()),
    path("create/", AllergenCreate.as_view()),
    path("<int:pk>/", AllergenDetail.as_view()),
]

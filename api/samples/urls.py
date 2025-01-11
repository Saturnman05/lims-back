from django.urls import path

from .views import SampleListCreate

urlpatterns = [
    path("", SampleListCreate.as_view()),
]

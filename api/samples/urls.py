from django.urls import path

from .views import SampleListCreate, SampleDetail

urlpatterns = [
    path("", SampleListCreate.as_view()),
    path("<int:pk>/", SampleDetail.as_view()),
]

from django.urls import path

from .views import SampleCreate, SampleDetail, SampleList

urlpatterns = [
    path("create/", SampleCreate.as_view()),
    path("", SampleList.as_view()),
    path("<int:pk>/", SampleDetail.as_view()),
]

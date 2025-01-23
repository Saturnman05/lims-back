from django.urls import path

from .views import SampleCreate, SampleDetail, SampleList, sample_update

urlpatterns = [
    path("update/", sample_update),
    path("create/", SampleCreate.as_view()),
    path("<int:pk>/", SampleDetail.as_view()),
    path("", SampleList.as_view()),
]

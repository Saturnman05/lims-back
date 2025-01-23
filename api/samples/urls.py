from django.urls import path

from .views import SampleCreate, SampleDetail, SampleList, sample_update, sample_assignment

urlpatterns = [
    path("update/", sample_update),
    path("create/", SampleCreate.as_view()),
    path("<int:pk>/", SampleDetail.as_view()),
    path("", SampleList.as_view()),
    path('sample-assignment/', sample_assignment),
    path('sample-assignment/<int:sample_id>/', sample_assignment),
]

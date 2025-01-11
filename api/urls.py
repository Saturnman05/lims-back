from django.urls import path, include

urlpatterns = [
    path("users/", include("api.users.urls")),
    path("allergens/", include("api.allergens.urls")),
]

from django.urls import path, include

urlpatterns = [
    path("users/", include("api.users.urls")),
    path("roles/", include("api.users.roles.urls")),
    path("categorys/", include("api.samples.categorys.urls")),
    path("subcategorys/", include("api.samples.subcategorys.urls")),
    path("files/", include("api.samples.files.urls")),
    path("samples/", include("api.samples.urls")),
]

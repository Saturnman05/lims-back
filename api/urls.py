from django.urls import path, include

urlpatterns = [
    path("users/", include("api.users.urls")),
    path("allergens/", include("api.samples.allergens.urls")),
    path("categorys/", include("api.samples.categorys.urls")),
    path("ingredients/", include("api.samples.ingredients.urls")),
    path("samples/", include("api.samples.urls")),
]

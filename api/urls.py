from django.urls import path, include

urlpatterns = [
    path("users/", include("api.users.urls")),
    path("allergens/", include("api.allergens.urls")),
    path("categorys/", include("api.categorys.urls")),
    path("ingredients/", include("api.ingredients.urls")),
    path("samples/", include("api.samples.urls")),
]

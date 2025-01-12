from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from nested_admin.nested import NestedStackedInline, NestedModelAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

from .samples.allergens.models import Allergens, AllergenSample
from .samples.categorys.models import Category, CategorySample
from .samples.ingredients.models import Ingredient, SampleIngredient
from .samples.models import Sample


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "full_name",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("full_name",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("full_name",)}),)


class AllergenSampleInline(NestedStackedInline):
    model = AllergenSample
    extra = 1


class CategorySampleInline(NestedStackedInline):
    model = CategorySample
    extra = 1


class SampleIngredientInline(NestedStackedInline):
    model = SampleIngredient
    extra = 1


class SampleAdmin(NestedModelAdmin):
    list_display = (
        "comercial_name",
        "product_brand",
        "get_allergens",
        "get_categorys",
        "get_ingredients",
    )

    inlines = [AllergenSampleInline, CategorySampleInline, SampleIngredientInline]

    def get_allergens(self, obj):
        return ", ".join([allergen.allergen_name for allergen in obj.allergens.all()])

    def get_categorys(self, obj):
        return ", ".join([category.category_name for category in obj.categorys.all()])

    def get_ingredients(self, obj):
        return ", ".join(
            [ingredient.ingredient_name for ingredient in obj.ingredients.all()]
        )

    get_allergens.short_description = "Alérgenos"
    get_categorys.short_description = "Categorias"
    get_ingredients.short_description = "Categorias"


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Allergens)
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Sample, SampleAdmin)

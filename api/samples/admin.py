from nested_admin.nested import NestedStackedInline, NestedModelAdmin

from .allergens.models import AllergenSample
from .categorys.models import CategorySample
from .ingredients.models import SampleIngredient


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

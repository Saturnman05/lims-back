from nested_admin.nested import NestedStackedInline, NestedModelAdmin

from .categorys.models import CategorySample
from .subcategorys.models import SubcategorySample


class CategorySampleInline(NestedStackedInline):
    model = CategorySample
    extra = 1


class SubcategorySampleInline(NestedStackedInline):
    model = SubcategorySample
    extra = 1


class SampleAdmin(NestedModelAdmin):
    pk_field = "sample_id"
    list_display = (
        "comercial_name",
        "product_brand",
        "get_categorys",
        "get_subcategorys",
    )

    inlines = [CategorySampleInline, SubcategorySampleInline]

    def get_categorys(self, obj):
        return ", ".join([category.category_name for category in obj.categorys.all()])

    def get_subcategorys(self, obj):
        return ", ".join(
            [subcategory.subcategory_name for subcategory in obj.subcategorys.all()]
        )

    get_categorys.short_description = "Categorias"
    get_subcategorys.short_description = "Subcategorias"

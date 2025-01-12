from django.contrib import admin

from .users.admin import CustomUserAdmin
from .models import CustomUser

from .samples.allergens.models import Allergens
from .samples.categorys.models import Category
from .samples.ingredients.models import Ingredient
from .samples.models import Sample
from .samples.admin import SampleAdmin


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Allergens)
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Sample, SampleAdmin)

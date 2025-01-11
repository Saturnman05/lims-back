from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

from .allergens.models import Allergens
from .categorys.models import Category
from .ingredients.models import Ingredient


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


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Allergens)
admin.site.register(Category)
admin.site.register(Ingredient)

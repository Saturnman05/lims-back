from django.contrib import admin

from .users.models import User
from .users.admin import CustomUserAdmin

from .samples.categorys.models import Category
from .samples.subcategorys.models import Subcategory
from .samples.files.models import File
from .samples.models import Sample
from .samples.admin import SampleAdmin


# admin.site.register(CustomUser, CustomUserAdmin)\
admin.site.register(User, CustomUserAdmin)

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(File)
admin.site.register(Sample, SampleAdmin)

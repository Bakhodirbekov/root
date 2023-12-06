from django.contrib import admin
from .models import Category # Import your model
from .models import SubCategory
from .models import Work

admin.site.register(Category) # Use register, not registor
admin.site.register(SubCategory)
admin.site.register(Work)
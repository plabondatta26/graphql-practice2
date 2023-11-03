from django.contrib import admin

from ingredients.models import Ingredient, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Ingredient)
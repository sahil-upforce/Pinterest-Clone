from django.contrib import admin

from pinterest.models import Category


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass

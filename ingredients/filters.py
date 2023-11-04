from .models import Category
import django_filters
from django_filters.rest_framework import FilterSet


class CategoryFilter(FilterSet):
    class Meta:
        model = Category
        fields = (
            "id",
            "name"
        )

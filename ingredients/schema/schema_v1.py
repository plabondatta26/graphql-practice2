from graphene import relay

from ingredients.models import Category, Ingredient
from graphene_django import DjangoObjectType


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "ingredients")
        description = "Represents a category."
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node,)


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")
        description = "Represents an ingredient."

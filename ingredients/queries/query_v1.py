import graphene

from ingredients.models import Ingredient, Category
from ingredients.schema.schema_v1 import IngredientType, CategoryType


class IngredientQuery(graphene.ObjectType):
    ingredients = graphene.List(IngredientType)

    def resolve_ingredients(self, info):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related("category").all()


class CategoryQuery(graphene.ObjectType):
    category = graphene.Field(CategoryType, pk=graphene.String(), name=graphene.String())

    def resolve_category(self, info, pk=None, name=None):
        """
        Resolver for fetching a category by ID or name.
        """
        if pk:
            return Category.objects.filter(id=pk).first()
        elif name:
            return Category.objects.filter(name__contains=name)
        return Category.objects.all()

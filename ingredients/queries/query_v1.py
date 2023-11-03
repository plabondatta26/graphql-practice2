import graphene

from ingredients.models import Ingredient, Category
from ingredients.schema.schema_v1 import IngredientType, CategoryType


#
#     category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

class IngredientQuery(graphene.ObjectType):
    ingredients = graphene.List(IngredientType)

    def resolve_ingredients(self, info):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related("category").all()


class CategoryQuery(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))
    category_by_id = graphene.Field(CategoryType, id=graphene.String(required=True))

    def resolve_categories(self, info):
        return Category.objects.all()

    def resolve_category_by_name(self, info, name):
        return Category.objects.filter(name__contains=name)

    def resolve_category_by_id(self, info, id):
        return Category.objects.filter(id=id).first()

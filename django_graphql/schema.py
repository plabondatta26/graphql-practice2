import graphene

from ingredients.models import Ingredient, Category
from ingredients.queries.query_v1 import IngredientQuery, CategoryQuery
from ingredients.schema.schema_v1 import IngredientType, CategoryType


class Query(IngredientQuery, CategoryQuery):
    pass
    # all_ingredients = graphene.List(IngredientType)
    # category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))
    #
    # def resolve_all_ingredients(root, info):
    #     print(info)
    #     # We can easily optimize query count in the resolve method
    #     return Ingredient.objects.select_related("category").all()
    #
    # def resolve_category_by_name(root, info, name):
    #     try:
    #         return Category.objects.get(name=name)
    #     except Category.DoesNotExist:
    #         return None


schema = graphene.Schema(query=Query)

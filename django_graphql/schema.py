import graphene
from ingredients.queries.query_v1 import IngredientQuery, CategoryQuery


class Query(IngredientQuery, CategoryQuery):
    pass


schema = graphene.Schema(query=Query)

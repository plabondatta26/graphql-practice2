import graphene
from ingredients.queries.query_v1 import IngredientQuery, CategoryQuery, CategoryMutation


class Query(IngredientQuery, CategoryQuery):
    pass


class Mutation(graphene.ObjectType):
    category_mutation = CategoryMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

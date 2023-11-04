import graphene
from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django_extras import DjangoObjectField, DjangoFilterListField, DjangoFilterPaginateListField

from ingredients.custom_paginator import CustomGraphenePaginator
from ingredients.filters import CategoryFilter
from ingredients.models import Ingredient, Category
from ingredients.schema.schema_v1 import IngredientType, CategoryType


class IngredientQuery(graphene.ObjectType):
    ingredients = graphene.List(IngredientType)

    def resolve_ingredients(self, info):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related("category").all()


class CategoryQuery(graphene.ObjectType):
    retrieve_category = graphene.Field(CategoryType, pk=graphene.Int(required=True))
    all_categories = DjangoFilterConnectionField(CategoryType, page=graphene.Int(), page_size=graphene.Int())

    def resolve_retrieve_category(self, info, pk):
        if info.context.user.is_authenticated:
            return Category.objects.filter(pk=pk).first()
        else:
            raise Exception("You do not have permission to view")

    def resolve_all_categories(self, info, page=None, page_size=None, **kwargs):
        if info.context.user.is_authenticated:
            queryset = Category.objects.all()
            info.context.success_message = "successfully get"
            info.context.error_message = "successfully error"
            data, info = CustomGraphenePaginator.paginate_data(queryset, page, page_size)
            return data
            # return queryset
        else:
            raise Exception("You do not have permission to view")


class CategoryMutation(graphene.Mutation):
    class Arguments:
        pk = graphene.Int()
        name = graphene.String()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, pk=None, name=None):
        if pk and name:
            # Update category
            category_obj = Category.objects.filter(id=pk).first()
            if category_obj:
                category_obj.name = name
                category_obj.save()
                return CategoryMutation(category=category_obj)
            else:
                raise Exception(f"Category with id {id} does not exist.")
        elif name:
            # Create category
            category_obj = Category(name=name)
            category_obj.save()
            return CategoryMutation(category=category_obj)
        else:
            raise Exception("Name is required for creating a new category.")

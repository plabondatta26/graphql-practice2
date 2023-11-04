import graphene


class PageInfo(graphene.ObjectType):
    total_count = graphene.Int()
    current_page = graphene.Int()
    has_next_page = graphene.Boolean()
    next_page_number = graphene.Int()


class CustomGraphenePaginator:
    @staticmethod
    def get_queryset(queryset, instance_list):
        pk_list = [instance.pk for instance in instance_list]
        return queryset.filter(pk__in=pk_list)

    @staticmethod
    def paginate_data(queryset, page, page_size):
        total_count = queryset.count()
        if page and page_size:
            start_index = (page - 1) * page_size
            end_index = start_index + page_size
            paginated_data = list(queryset[start_index:end_index])
            has_next_page = end_index < total_count
            next_page_number = page + 1 if has_next_page else None
            page_info = PageInfo(
                total_count=total_count,
                current_page=page,
                has_next_page=has_next_page,
                next_page_number=next_page_number,
            )
            return CustomGraphenePaginator.get_queryset(queryset, paginated_data), page_info
        return queryset

# def get_custom_queryset(queryset, instance_list):
#     obj = QuerySetFromList(queryset=queryset, instance_list=instance_list)
#     return obj.get_queryset()

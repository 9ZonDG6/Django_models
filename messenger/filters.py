import django_filters
from django.db.models import Q, Count
from django.db.models.functions import Length


class PostFilter(django_filters.FilterSet):
    author = django_filters.CharFilter(field_name='author__nickname', lookup_expr='icontains', label='Автор поста')
    term = django_filters.CharFilter(label='Поиск по содержимому', method='filter_term')
    post_length_gte = django_filters.NumberFilter(method='filter_by_length_gte', label='Кол-во символов в посте от')
    post_length_lte = django_filters.NumberFilter(method='filter_by_length_lte', label='Кол-во символов в посте до')
    has_comments = django_filters.BooleanFilter(method='filter_has_comment', label='Наличие комментарий')

    @staticmethod
    def filter_by_length_gte(queryset, name, value):
        queryset = queryset.annotate(post_length=Length('post_text'))
        return queryset.filter(post_length__gte=value)

    @staticmethod
    def filter_by_length_lte(queryset, name, value):
        queryset = queryset.annotate(post_length=Length('post_text'))
        return queryset.filter(post_length__lte=value)

    @staticmethod
    def filter_term(queryset, name, value):
        criteria = Q()
        for term in value.split():
            criteria &= Q(post_subject__icontains=term) | Q(post_text__icontains=term)
        return queryset.filter(criteria).distinct()

    @staticmethod
    def filter_has_comment(queryset, name, value):
        queryset = queryset.annotate(num_comments=Count('comments'))
        if value:
            return queryset.filter(num_comments=value)
        else:
            return queryset.filter(num_comments=0)

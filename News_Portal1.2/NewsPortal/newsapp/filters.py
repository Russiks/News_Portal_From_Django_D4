"""Классы, в которых указываем, как можно фильтровать данные моделей."""
# import django_filters
from django.forms import DateTimeInput
from django_filters import (
    FilterSet, DateFilter, DateTimeFromToRangeFilter, DateTimeFilter, CharFilter, ModelChoiceFilter,
    ModelMultipleChoiceFilter
)
from django_filters.widgets import (
    DateRangeWidget, RangeWidget
)
from .models import (
    Author, Post, Category
)


class PostFilter(FilterSet):
    searchTitle = CharFilter(
        max_length=128,
        field_name='title',
        lookup_expr='icontains',
        label='Поиск по оглавлению',
    )

    filterAuthor = ModelChoiceFilter(
        field_name='author',
        queryset=Author.objects.all(),
        label='',
        empty_label='Выбор автора'
    )

    # Category = ModelMultipleChoiceFilter(
    #     field_name='name',
    #     queryset=categoryType.objects.all(),
    # )

    # Post.objects.filter(categoryType='NW').values('categoryType'),
    # Вариант с использованием среза по датам с ключом 'exact'
    filterDate = DateTimeFromToRangeFilter(
        field_name='dateCreation',
        lookup_expr='exact',
        label='Поиск по дате',
        widget=RangeWidget(
            attrs={'type': 'datetime-local'}
        )
    )

    #________________________________________________________________________
    # Вариант без использования среза по датам с ключом 'gt'
    # filterDate = DateTimeFilter(
    #     field_name='dateCreation', lookup_expr='gt', widget=DateTimeInput(
    #         format='%Y-%m-%dT%H:%M',
    #         attrs={'type': 'datetime-local'}, ),
    # )
    # ________________________________________________________________________

    class Meta:
        model = Post
        fields = {
            # 'title': ['icontains'],
            # 'author': ['exact'],
            'categoryType': ['exact'],
            # 'dateCreation': ['gte'],  # Поиск по дате организован через переменную filterDate с использованием
            # фильтра Django - DateTimeFromToRangeFilter или DateTimeFilter
        }

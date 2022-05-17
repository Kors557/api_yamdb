from asyncore import loop
from django_filters import FilterSet, AllValuesFilter

from reviews.models import Title


class TitleFilter(FilterSet):
    genre = AllValuesFilter(field_name='genre__slug')
    category = AllValuesFilter(field_name='category__slug')

    class Meta:
        model = Title
        fields = ('category', 'genre', 'name', 'year')

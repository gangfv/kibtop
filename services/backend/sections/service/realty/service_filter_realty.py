from sections.models import RealtyFull

import django_filters


class FilterRealty(django_filters.FilterSet):
    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    sub_category_en = django_filters.CharFilter()
    sub_category_ru = django_filters.CharFilter()
    sub_category_tr = django_filters.CharFilter()
    sell_type = django_filters.CharFilter()
    all_old_new = django_filters.CharFilter()
    number_rooms = django_filters.CharFilter()

    class Meta:
        model = RealtyFull
        fields = ['price', 'sub_category_en', 'sub_category_ru', 'sub_category_tr', 'sell_type', 'all_old_new', 'number_rooms']

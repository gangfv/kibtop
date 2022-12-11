from sections.models import WorkFull

import django_filters


class FilterWork(django_filters.FilterSet):
    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    sub_apartment_en = django_filters.CharFilter()
    sub_apartment_ru = django_filters.CharFilter()
    sub_apartment_tr = django_filters.CharFilter()
    for_work_type_en = django_filters.CharFilter()
    for_work_type_ru = django_filters.CharFilter()
    for_work_type_tr = django_filters.CharFilter()
    employment_en = django_filters.CharFilter()
    employment_ru = django_filters.CharFilter()
    employment_tr = django_filters.CharFilter()

    class Meta:
        model = WorkFull
        fields = [
            'price', 'sub_apartment_en', 'sub_apartment_ru', 'sub_apartment_tr', 'for_work_type_en',
            'for_work_type_ru', 'for_work_type_tr', 'employment_en', 'employment_ru', 'employment_tr',
        ]

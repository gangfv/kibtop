from sections.models import ChildrenFull, ChildrenFullFavouritesUser, ChildrenFullViewsUser

import django_filters


class FilterChildren(django_filters.FilterSet):
    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    sub_category_en = django_filters.CharFilter()
    sub_category_ru = django_filters.CharFilter()
    sub_category_tr = django_filters.CharFilter()

    class Meta:
        model = ChildrenFull
        fields = ['price', 'sub_category_en', 'sub_category_ru', 'sub_category_tr']


class FilterChildrenViews(django_filters.FilterSet):
    avto_full = django_filters.NumberFilter()
    user = django_filters.NumberFilter()

    class Meta:
        model = ChildrenFullViewsUser
        fields = ['avto_full', 'user']


class FilterChildrenFavourites(django_filters.FilterSet):
    avto_full = django_filters.NumberFilter()
    user = django_filters.NumberFilter()

    class Meta:
        model = ChildrenFullFavouritesUser
        fields = ['avto_full', 'user']

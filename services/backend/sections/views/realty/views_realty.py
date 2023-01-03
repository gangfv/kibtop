from rest_framework import generics
from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from sections.models import (
    RealtyFull, RealtyFullFavouritesUser, RealtyFullViewsUser
)
from sections.serializer import (
    RealtyFullSerializerDetail, RealtyFullSerializerEN, RealtyFullSerializerRU,
    RealtyFullSerializerTR, RealtyFullSerializer, RealtyFullViewsUserSerializer, RealtyFullFavouritesUserSerializer
)
from sections.service import (
    FilterRealty, FilterRealtyFavourites, FilterRealtyViews
)
from sections.utils import query_list_lang

model_realty = RealtyFull.objects.filter(publisher=True,)


class RealtyLimitPagination(MultipleModelLimitOffsetPagination):
    default_limit = 10


class RealtyFullAPIList(ObjectMultipleModelAPIView, generics.ListAPIView):
    serializer_class = RealtyFullSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FilterRealty
    pagination_class = RealtyLimitPagination

    def get_querylist(self):

        query = self.request.query_params

        querylist_full = [
            {
                'queryset': model_realty,
                'serializer_class': RealtyFullSerializerEN,
                'label': 'en',
            },
            {
                'queryset': model_realty,
                'serializer_class': RealtyFullSerializerRU,
                'label': 'ru',
            },
            {
                'queryset': model_realty,
                'serializer_class': RealtyFullSerializerTR,
                'label': 'tr',
            },
        ]

        try:
            if query['lang'] == 'en':
                return query_list_lang(model_realty, RealtyFullSerializerEN, 'en')
            elif query['lang'] == 'ru':
                return query_list_lang(model_realty, RealtyFullSerializerRU, 'ru')
            elif query['lang'] == 'tr':
                return query_list_lang(model_realty, RealtyFullSerializerTR, 'tr')
            return querylist_full
        except Exception:
            return querylist_full


class RealtyFullAPIListCreate(generics.CreateAPIView):
    queryset = model_realty
    serializer_class = RealtyFullSerializerDetail
    permission_classes = (IsAuthenticatedOrReadOnly,)


class RealtyFullAPIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = model_realty
    serializer_class = RealtyFullSerializerDetail
    permission_classes = (IsAuthenticatedOrReadOnly,)


class RealtyFullViewsUserAPIList(generics.ListCreateAPIView):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FilterRealtyViews
    queryset = RealtyFullViewsUser.objects.all()
    serializer_class = RealtyFullViewsUserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class RealtyFullFavouritesUserAPIList(generics.ListCreateAPIView):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FilterRealtyFavourites
    queryset = RealtyFullFavouritesUser.objects.all()
    serializer_class = RealtyFullFavouritesUserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class RealtyFullFavouritesUserAPIUpdateDestroy(generics.DestroyAPIView):
    queryset = RealtyFullFavouritesUser.objects.all()
    serializer_class = RealtyFullFavouritesUserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
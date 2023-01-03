from rest_framework import generics
from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination
from drf_multiple_model.views import ObjectMultipleModelAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from sections.models import (
    ChildrenFull, ChildrenFullFavouritesUser, ChildrenFullViewsUser
)
from sections.serializer import (
    ChildrenFullSerializer, ChildrenFullSerializerEN, ChildrenFullSerializerRU,
    ChildrenFullSerializerTR, ChildrenFullSerializerDetail, ChildrenFullFavouritesUserSerializer,
    ChildrenFullViewsUserSerializer
)
from sections.service import (
    FilterChildren, FilterChildrenViews, FilterChildrenFavourites
)
from sections.utils import query_list_lang

model_children = ChildrenFull.objects.filter(publisher=True)


class ChildrenLimitPagination(MultipleModelLimitOffsetPagination):
    default_limit = 10


class ChildrenFullAPIList(ObjectMultipleModelAPIView, generics.ListAPIView):
    serializer_class = ChildrenFullSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FilterChildren
    pagination_class = ChildrenLimitPagination

    def get_querylist(self):

        query = self.request.query_params

        querylist_full = [
            {
                'queryset': model_children,
                'serializer_class': ChildrenFullSerializerEN,
                'label': 'en',
            },
            {
                'queryset': model_children,
                'serializer_class': ChildrenFullSerializerRU,
                'label': 'ru',
            },
            {
                'queryset': model_children,
                'serializer_class': ChildrenFullSerializerTR,
                'label': 'tr',
            },
        ]

        try:
            if query['lang'] == 'en':
                return query_list_lang(model_children, ChildrenFullSerializerEN, 'en')
            elif query['lang'] == 'ru':
                return query_list_lang(model_children, ChildrenFullSerializerRU, 'ru')
            elif query['lang'] == 'tr':
                return query_list_lang(model_children, ChildrenFullSerializerTR, 'tr')
            return querylist_full
        except Exception:
            return querylist_full


class ChildrenFullAPIListCreate(generics.CreateAPIView):
    queryset = model_children
    serializer_class = ChildrenFullSerializerDetail
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ChildrenFullAPIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = model_children
    serializer_class = ChildrenFullSerializerDetail
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ChildrenFullViewsUserAPIList(generics.ListCreateAPIView):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FilterChildrenViews
    queryset = ChildrenFullViewsUser.objects.all()
    serializer_class = ChildrenFullViewsUserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ChildrenFullFavouritesUserAPIList(generics.ListCreateAPIView):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FilterChildrenFavourites
    queryset = ChildrenFullFavouritesUser.objects.all()
    serializer_class = ChildrenFullFavouritesUserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ChildrenFullFavouritesUserAPIUpdateDestroy(generics.DestroyAPIView):
    queryset = ChildrenFullFavouritesUser.objects.all()
    serializer_class = ChildrenFullFavouritesUserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

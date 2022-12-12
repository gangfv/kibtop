from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from sections.models import ElectronicsFull
from sections.serializer import (
    ElectronicsFullSerializer, ElectronicsFullSerializerEN, ElectronicsFullSerializerRU, ElectronicsFullSerializerTR, ElectronicsFullSerializerDetail
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from sections.service import FilterElectronics
from sections.utils import query_list_lang

model_electronics = ElectronicsFull.objects.all()


class ElectronicsLimitPagination(MultipleModelLimitOffsetPagination):
    default_limit = 10


class ElectronicsFullAPIList(ObjectMultipleModelAPIView, generics.ListAPIView):
    serializer_class = ElectronicsFullSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FilterElectronics
    pagination_class = ElectronicsLimitPagination

    def get_querylist(self):

        query = self.request.query_params

        querylist_full = [
            {
                'queryset': model_electronics,
                'serializer_class': ElectronicsFullSerializerEN,
                'label': 'en',
            },
            {
                'queryset': model_electronics,
                'serializer_class': ElectronicsFullSerializerRU,
                'label': 'ru',
            },
            {
                'queryset': model_electronics,
                'serializer_class': ElectronicsFullSerializerTR,
                'label': 'tr',
            },
        ]

        try:
            if query['lang'] == 'en':
                return query_list_lang(model_electronics, ElectronicsFullSerializerEN, 'en')
            elif query['lang'] == 'ru':
                return query_list_lang(model_electronics, ElectronicsFullSerializerRU, 'ru')
            elif query['lang'] == 'tr':
                return query_list_lang(model_electronics, ElectronicsFullSerializerTR, 'tr')
            return querylist_full
        except Exception:
            return querylist_full


class ElectronicsFullAPIListCreate(generics.CreateAPIView):
    queryset = model_electronics
    serializer_class = ElectronicsFullSerializerDetail
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ElectronicsFullAPIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = model_electronics
    serializer_class = ElectronicsFullSerializerDetail
    permission_classes = (IsAuthenticatedOrReadOnly,)

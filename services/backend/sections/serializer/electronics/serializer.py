from rest_framework import serializers

from sections.models import (
    ElectronicsFull, ElectronicsFullUpload, ElectronicsFullViewsUser,
    ElectronicsFullFavouritesUser
)


class ElectronicsFullUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectronicsFullUpload
        fields = ('uploads',)


class ElectronicsFullViewsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectronicsFullViewsUser
        fields = '__all__'


class ElectronicsFullFavouritesUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectronicsFullFavouritesUser
        fields = '__all__'


class ElectronicsFullSerializerDetail(serializers.ModelSerializer):
    electronics_full_upload = ElectronicsFullUploadSerializer(many=True)

    class Meta:
        model = ElectronicsFull
        fields = '__all__'


class ElectronicsFullSerializerEN(serializers.ModelSerializer):
    class Meta:
        model = ElectronicsFull
        fields = ('id', 'title_en','description_en', 'created_at', 'updated_at', 'address',
                  'price', 'upload', 'sub_category_en', 'category_en', 'recommend', 'publisher')


class ElectronicsFullSerializerRU(serializers.ModelSerializer):
    class Meta:
        model = ElectronicsFull
        fields = ('id', 'title_ru', 'description_ru','created_at', 'updated_at', 'address',
                  'price', 'upload', 'sub_category_ru', 'category_ru', 'recommend', 'publisher')


class ElectronicsFullSerializerTR(serializers.ModelSerializer):
    class Meta:
        model = ElectronicsFull
        fields = ('id', 'title_tr','description_tr', 'created_at', 'updated_at', 'address',
                  'price', 'upload', 'sub_category_tr', 'category_tr', 'recommend', 'publisher')


class ElectronicsFullSerializer(serializers.Serializer):
    en = ElectronicsFullSerializerEN(many=True)
    ru = ElectronicsFullSerializerRU(many=True)
    tr = ElectronicsFullSerializerTR(many=True)

from dataclasses import field
from rest_framework import serializers
from .models import *



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagModel
        fields = '__all__'


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariants
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    varients = serializers.SerializerMethodField()
    class Meta:
        model = ProductModel
        fields = '__all__'


    def get_varients(self,obj):
        print("get_varients of product :>  ",obj.id)

        v_obj = ProductVariants.objects.filter(product=obj.id)
        v_qs = ProductVariantSerializer(v_obj, many=True)

        return v_qs.data


        
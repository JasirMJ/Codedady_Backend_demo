from rest_framework import serializers

from relations.models import ProductsRelationModel, TagsModel, ProductVariant


class TagsSerializers(serializers.ModelSerializer):

    class Meta:
        model = TagsModel
        # fields = ["id","name", "price", "description" ]
        fields="__all__"

class ProductVariantSerializers(serializers.ModelSerializer):

    class Meta:
        model = ProductVariant
        # fields = ["id","name", "price", "description" ]
        fields="__all__"


class ProductSerializers(serializers.ModelSerializer):
    tags = TagsSerializers(many=True)
    varients = serializers.SerializerMethodField()

    class Meta:
        model = ProductsRelationModel
        # fields = ["id","name", "price", "description" ]
        fields="__all__"

    def get_varients(self,obj):
        print("get_varients of product :>  ",obj.id)

        v_obj = ProductVariant.objects.filter(product=obj)
        v_qs = ProductVariantSerializers(v_obj, many=True)

        # for x in v_obj:
        #     print(x.id,x.product.id,x.price,)

        return v_qs.data
from rest_framework import serializers

from relations.models import TagsModel
from relations.models import ProductsRelationModel


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductsRelationModel
        # fields = ["id","name", "price", "description" ]
        fields="__all__"


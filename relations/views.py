from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from relations.models import *
from relations.serializers import TagsSerializers, ProductVariantSerializers
from relations.serializers import ProductSerializers


class ProductSAPI(ListAPIView):
    serializer_class = ProductSerializers

    def get_queryset(self):
    #     which returns a queryset
        qs = ProductsRelationModel.objects.all()

        id = self.request.GET.get("id","")
        name = self.request.GET.get("name","")
        price = self.request.GET.get("price","")
        description = self.request.GET.get("description","")

        if id: qs = qs.filter(id=id)

        # m2m filteration with tags
        if name: qs = qs.filter( Q( name=name ) | Q(tags__name=name))

        if price: qs = qs.filter(price=price)
        if description: qs = qs.filter(description=description)

        return qs

    # def get(self,request):
    #     p_qs = ProductsRelationModel.objects.all()
    #     data = ProductSerializers(p_qs).data
    #     return Response({
    #         "data":data
    #     })

    def post(self,request):
        print("Request Data : ",self.request.data)
        id = self.request.POST.get("id", "")
        if id:
            qs_to_modify = ProductsRelationModel.objects.filter(id=id)
            if qs_to_modify.count():
                obj_to_modify = qs_to_modify.first()
                p_obj = ProductSerializers(obj_to_modify, data=self.request.data, partial=True)
                msg = "Updated Successfully"
            else:
                return Response({ "Status":False, "Message":"No record found with the id" })
        else:
            p_obj = ProductSerializers(data=self.request.data, partial=True)
            msg = "Saved Successfully"

        p_obj.is_valid(raise_exception=True)
        obj = p_obj.save()
        saved_data = ProductSerializers(obj).data

        return Response({
            "Status":True,
            "Message":msg,
            "Data":self.request.data,
            "saved":saved_data,
        })



    def put(self,request):
        print("Request Data : ", self.request.data)
        id = self.request.POST.get("id","")
        qs_to_modify = ProductsRelationModel.objects.filter(id=id)
        if qs_to_modify.count(): obj_to_modify = qs_to_modify.first()
        else:
            return Response({
                "Status":False,
                "Message":"No record found with id "+ id
            })

        p_obj = ProductSerializers(obj_to_modify,data=self.request.data, partial=True)
        p_obj.is_valid(raise_exception=True)
        obj = p_obj.save()
        print("obj ", obj)
        saved_data = ProductSerializers(obj).data
        return Response({
            "Status": True,
            "Message": "Updated Successfully",
            "Data": self.request.data,
            "saved": saved_data,
        })

    def delete(self,request):

        id= request.GET.get('id',"")

        p_qs = ProductsRelationModel.objects.filter(id=id)
        p_qs.delete()

        return Response({
            "Status":True,
            "Message":"data Deleted "
        })


class TagsAPI(ListAPIView):
    serializer_class = TagsSerializers

    def get_queryset(self):
        qs = TagsModel.objects.all()
        return qs


    def post(self,request):
        print("Request Data : ",self.request.data)
        id = self.request.POST.get("id", "")


        if id:
            qs_to_modify = TagsModel.objects.filter(id=id)
            if qs_to_modify.count():
                obj_to_modify = qs_to_modify.first()
                p_obj = TagsSerializers(obj_to_modify, data=self.request.data, partial=True)
                msg = "Updated Successfully"
            else:
                return Response({ "Status":False, "Message":"No record found with the id" })
        else:
            p_obj = TagsSerializers(data=self.request.data, partial=True)
            msg = "Saved Successfully"

        p_obj.is_valid(raise_exception=True)
        obj = p_obj.save()
        saved_data = TagsSerializers(obj).data


        return Response({
            "Status":True,
            "Message":msg,
            "Data":self.request.data,
            "saved":saved_data,
        })

    def patch(self,request):
        try:
            msg=1
            productid = self.request.POST["productid"]
            tagid = self.request.POST["tagid"]
            keyword = self.request.POST["keyword"]

            t_qs = TagsModel.objects.filter(id=tagid)
            if len(t_qs)==0:return Response({"Status":False,"Message":"Tag not found"})

            p_qs = ProductsRelationModel.objects.filter(id=productid)
            if len(p_qs)==0:return Response({"Status":False,"Message":"Product not found"})

            p_obj = p_qs[0]

            if keyword == "add": p_obj.tags.add(t_qs[0])

            if keyword == "remove": p_obj.tags.remove(t_qs[0])

        except Exception as e:
            msg = str(e)


        return Response({
            "Status":True,
            "Message":msg,
        })


STATUS = "Status"
MESSAGE = "Message"

class ProductVariantAPI(ListAPIView):
    serializer_class = ProductVariantSerializers

    def get_queryset(self):


        qs = ProductVariant.objects.all()

        print(qs[0].product.name)

        return qs


    def post(self,request):
        print("Request Data : ",self.request.data)
        try:
            id = self.request.POST.get("id", "")

            product = self.request.POST["product"]
        except Exception as e :
            return Response({STATUS:1,MESSAGE:str(e)})

        p_qs = ProductsRelationModel.objects.filter(id=product)
        if len(p_qs) ==0:return Response({STATUS:0,MESSAGE:"No record found for product with privuded id"})
        # validate for product


        if id:
            qs_to_modify = ProductVariant.objects.filter(id=id)
            if qs_to_modify.count():
                obj_to_modify = qs_to_modify.first()
                p_obj = ProductVariantSerializers(obj_to_modify, data=self.request.data, partial=True)
                msg = "Updated Successfully"
            else:
                return Response({ "Status":False, "Message":"No record found with the id" })
        else:
            p_obj = ProductVariantSerializers(data=self.request.data, partial=True)
            msg = "Saved Successfully"

        p_obj.is_valid(raise_exception=True)
        obj = p_obj.save(product=p_qs[0])
        saved_data = ProductVariantSerializers(obj).data


        return Response({
            "Status":True,
            "Message":msg,
            "Data":self.request.data,
            "saved":saved_data,
        })

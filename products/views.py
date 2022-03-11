from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from products.serializers import *
from .models import *
from django.db.models import Q


# Create your views here.

class TagsAPI(ListAPIView):
    serializer_class = TagSerializer
    def post(self,request):
        id = self.request.POST.get("id","")

        if id:
            qs_to_modify = TagModel.objects.filter(id=id)
            if qs_to_modify.count():
                obj_to_modify = qs_to_modify.first()
                p_obj = TagSerializer(obj_to_modify, data=self.request.data, partial=True)
                msg = "Updated Successfully"
            else:
                return Response({ "Status":False, "Message":"No record found with the id" })
        else:
            p_obj = TagSerializer(data=self.request.data, partial=True)
            msg = "Saved Successfully"

        p_obj.is_valid(raise_exception=True)
        obj = p_obj.save()
        saved_data = TagSerializer(obj).data


        return Response({
            "Status":True,
            "Message" : msg,
            "Data" : saved_data
        })

    def get_queryset(self):
       
        
        datas = TagModel.objects.all()
        return datas


    def patch(self,request):
        try:
            msg=1
            productid = self.request.POST["productid"]
            tagid = self.request.POST["tagid"]
            keyword = self.request.POST["keyword"]

            t_qs = TagModel.objects.filter(id=tagid)
            if len(t_qs)==0:return Response({"Status":False,"Message":"Tag not found"})

            p_qs = ProductModel.objects.filter(id=productid)
            if len(p_qs)==0:return Response({"Status":False,"Message":"Product not found"})

            p_obj = p_qs[0]

            if keyword == "add": p_obj.tags.add(tagid)
            # if keyword == "add": p_obj.tags.add(t_qs[0])

            if keyword == "remove": p_obj.tags.remove(t_qs[0])

        except Exception as e:
            msg = str(e)


        return Response({
            "Status":True,
            "Message":msg,
        })


class ProductsAPI(ListAPIView):

    serializer_class = ProductSerializer

    def post(self,request):
        
        id = self.request.POST.get("id", "")
        if id:
            qs_to_modify = ProductModel.objects.filter(id=id)
            if qs_to_modify.count():
                obj_to_modify = qs_to_modify.first()
                p_obj = ProductSerializer(obj_to_modify, data=self.request.data, partial=True)
                msg = "Updated Successfully"
            else:
                return Response({ "Status":False, "Message":"No record found with the id" })
        else:
            p_obj = ProductSerializer(data=self.request.data, partial=True)
            msg = "Saved Successfully"

        p_obj.is_valid(raise_exception=True)
        obj = p_obj.save()
        saved_data = ProductSerializer(obj).data

        return Response({
            "Status":True,
            "Message":msg,
            "saved":saved_data,
        })

    
    def get_queryset(self):
        qs = ProductModel.objects.all()
        id = self.request.POST.get("id","")
        name = self.request.POST.get("name","")
        price = self.request.POST.get("price","")
        description = self.request.POST.get("description","")
        if id: qs = qs.filter(id=id)

        # m2m filteration with tags
        if name: qs = qs.filter( Q( name=name ) | Q(tags__name=name))

        if price: qs = qs.filter(price=price)
        if description: qs = qs.filter(description=description)

        return qs

STATUS = "Status"
MESSAGE = "Message"

class ProductVariantAPI(ListAPIView):
    serializer_class = ProductVariantSerializer
    def get_queryset(self):
        data = ProductVariants.objects.all()
        return data


    def post(self,reqquest):
        print("Request Data : ",self.request.data)
        try:
            id = self.request.POST.get("id", "")

            product = self.request.POST["product"]
        except Exception as e :
            return Response({STATUS:1,MESSAGE:str(e)})

        p_qs = ProductModel.objects.filter(id=product)
        if len(p_qs) ==0:return Response({STATUS:0,MESSAGE:"No record found for product with privuded id"})
        # validate for product


        if id:
            qs_to_modify = ProductVariants.objects.filter(id=id)
            if qs_to_modify.count():
                obj_to_modify = qs_to_modify.first()
                p_obj = ProductVariantSerializer(obj_to_modify, data=self.request.data, partial=True)
                msg = "Updated Successfully"
            else:
                return Response({ "Status":False, "Message":"No record found with the id" })
        else:
            p_obj = ProductVariantSerializer(data=self.request.data, partial=True)
            msg = "Saved Successfully"

        p_obj.is_valid(raise_exception=True)
        obj = p_obj.save(product=p_qs[0])
        saved_data = ProductVariantSerializer(obj).data


        return Response({
            "Status":True,
            "Message":msg,
            "saved":saved_data,
        })
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from simplecrud.models import ProductsModel
from simplecrudserializer.serializers import ProductSerializers


class ProductSAPI(ListAPIView):
    serializer_class = ProductSerializers

    def get_queryset(self):
    #     which returns a queryset
        qs = ProductsModel.objects.all()

        id = self.request.GET.get("id","")
        name = self.request.GET.get("name","")
        price = self.request.GET.get("price","")
        description = self.request.GET.get("description","")

        if id: qs = qs.filter(id=id)
        if name: qs = qs.filter(name__icontains=name)
        if price: qs = qs.filter(price=price)
        if description: qs = qs.filter(description=description)

        return qs

    # def get(self,request):
    #     p_qs = ProductsModel.objects.all()
    #     data = ProductSerializers(p_qs).data
    #     return Response({
    #         "data":data
    #     })

    def post(self,request):
        print("Request Data : ",self.request.data)
        id = self.request.POST.get("id", "")
        if id:
            qs_to_modify = ProductsModel.objects.filter(id=id)
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
        qs_to_modify = ProductsModel.objects.filter(id=id)
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

        p_qs = ProductsModel.objects.filter(id=id)
        p_qs.delete()

        return Response({
            "Status":True,
            "Message":"data Deleted "
        })
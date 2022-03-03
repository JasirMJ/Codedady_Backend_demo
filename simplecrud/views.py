from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from simplecrud.models import ProductsModel


class ProductAPI(ListAPIView):


    def get(self,request):
        try:

            # name = self.request.GET.get("name","default_name")
            # # name = self.request.GET['name']
            id = self.request.GET.get("id","")
            name = self.request.GET.get("name","")

            p_qs = ProductsModel.objects.all()

            if id: p_qs = p_qs.filter(id=id)

            if name: p_qs = p_qs.filter(name__icontains=name)

            print("Data ", p_qs)
            # print("Data ", p_qs[3])
            print("Data ", p_qs.first())

            data = []

            for x in p_qs:
                print("id : ",x.id)
                print("name : ",x.name)
                print("description : ",x.description)
                data.append(
                    {
                        'id':x.id,
                        'name':x.name,
                        'description':x.description,
                    }
                )
            # print("Type ", type(p_qs))
            # print("Type ", type(p_qs.first()))

            return Response({
                "Status":True,
                "Result : ":data,
            })

            # Add your logic here
        except Exception as e:
            msg = "Excepction occured "+str(e)
            return Response({
                "Status":False,
                "Message":msg,
            })
        # return Response([
        #     {
        #         "id":1,
        #         "name":name,
        #     },{
        #         "id":1,
        #         "name":"tanseer"+name   ,
        #     },
        # ])



    def post(self,request):
        print("Request Data : ",self.request.data)

        # name = self.request.POST.get('name')
        # or
        name = self.request.POST.get('name',"default")
        # name = self.request.data['name']
        price = self.request.POST.get('price',0.0)
        description = self.request.POST.get('description',"")



        return Response(name)
        # or
        # name = self.request.POST['name']

        p_obj = ProductsModel()
        p_obj = ProductsModel(
            name=name,
            price=price,
            description=description
        )
        # p_obj.name = name
        # p_obj.price = price
        # p_obj.description = description

        print("Obj ",p_obj)
        print("type Obj ",type(p_obj))

        p_obj.save()

        return Response({
            "Status":True,
            "Message":"Saved Successfully",
            "Data":self.request.data,
        })



    def put(self,request):
        print("Request Data : ",self.request.data)

        # name = self.request.POST.get('name')
        # or
        id = self.request.POST.get('id',"")
        name = self.request.POST.get('name',"default")
        price = self.request.POST.get('price',0.0)
        description = self.request.POST.get('description',"")
        # or
        # name = self.request.POST['name']

        p_obj = ProductsModel.objects.get(id=id)

        p_obj.name = name
        p_obj.price = price
        p_obj.description = description

        print("Obj ",p_obj)
        print("type Obj ",type(p_obj))

        p_obj.save()

        return Response({
            "Status":True,
            "Message":"Saved Successfully",
            "Data":self.request.data,
        })

    def delete(self,request):

        id= request.GET.get('id',"")

        p_qs = ProductsModel.objects.filter(id=id)
        p_qs.delete()

        return Response({
            "Status":True,
            "Message":"data Deleted "
        })
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import *
# Create your views here.

class StudentAPI(ListAPIView):

    def post(self,request):

        name = self.request.POST.get("name","")
        phone = self.request.POST.get("phone","")
        
        physics = self.request.POST.get("physics",0)
        chemistry = self.request.POST.get("chemistry",0)
        Maths = self.request.POST.get("Maths",0)
        Botany = self.request.POST.get("Botany",0)
        Zoology = self.request.POST.get("Zoology",0)
        English = self.request.POST.get("English",0)

        Total = int(physics) + int(chemistry) + int(Maths) + int(Botany) + int(Zoology) + int(English)
        if name == "":
            return Response({
                "status" : False,
                "Message" : "Please Fill your Name"
            })
        else:
            st_obj = student.objects.create(name=name,phone=phone)

            mark_obj = Marks.objects.create(student_id = st_obj.id,physics = physics,chemistry=chemistry,Maths=Maths,Botany=Botany,Zoology=Zoology,English=English,Total=Total)
            return Response({
                "status" : True,
                "Message" : "Succesfully Created User"
            })

    def get(self,request):

        id = self.request.POST.get("id","")

        if id == "":
            data = []
            st_obj = student.objects.all()
            mark_obj = Marks.objects.all()
            data = []
            for (x,y) in zip(st_obj,mark_obj):
                data.append(
                    {
                        'id':x.id,
                        'name':x.name,
                        'phone':x.phone,
                        "physics" : y.physics,
                        "chemistry" : y.chemistry,
                        "Maths" : y.Maths,
                        "Botany" : y.Botany,
                        "Zoology" : y.Zoology,
                        "English" : y.English,
                        "Total" : y.Total
                    }
            )
            return Response({

                "status" : True,
                "Your Result" :  data
            })
        
        else:
            data = []
            st_obj = student.objects.filter(id = id)
            mark_obj = Marks.objects.filter(student_id = id)
            for (x,y) in zip(st_obj,mark_obj):
                data.append(
                    {
                        'id':x.id,
                        'name':x.name,
                        'phone':x.phone,
                        "physics" : y.physics,
                        "chemistry" : y.chemistry,
                        "Maths" : y.Maths,
                        "Botany" : y.Botany,
                        "Zoology" : y.Zoology,
                        "English" : y.English,
                        "Total" : y.Total
                    }
                )

            return Response({
                "status" : True,
                "Your Data" : data
            })

    def put(self,request):
        
        id = self.request.POST.get("id","")

        name = self.request.POST.get("name","")
        phone = self.request.POST.get("phone","")
        
        physics = self.request.POST.get("physics",0)
        chemistry = self.request.POST.get("chemistry",0)
        Maths = self.request.POST.get("Maths",0)
        Botany = self.request.POST.get("Botany",0)
        Zoology = self.request.POST.get("Zoology",0)
        English = self.request.POST.get("English",0)
        Total = int(physics) + int(chemistry) + int(Maths) + int(Botany) + int(Zoology) + int(English)

        if id == "" or name == "" or phone == "" or physics == 0 or chemistry == 0 or Maths == 0 or Botany == 0 or Zoology == 0 or English == 0:
            return Response({
                "status" : False,
                "Message" :  "PLease Fill Your All Field"
            })
        else:
            st_obj = student.objects.get(id = id)
            mark_obj = Marks.objects.get(student_id= id)
            st_obj.name  = name
            st_obj.phone = phone
            mark_obj.phyiscs = physics
            mark_obj.chemistry = chemistry
            mark_obj.Maths = Maths
            mark_obj.Botany = Botany
            mark_obj.Zoology = Zoology
            mark_obj.English = English
            mark_obj.English = Total
            mark_obj.save()
            st_obj.save()


            return Response({
                "status" : True,
                "Message" : "Data Saved Succesfully"
            })

        
    def delete(self,request):

        id= self.request.POST.get('id',"")

        if id == "":
            return Response({
                "status" : False,
                "Message" :  "PLease Fill Your Id"
            })
        else:
            st_obj = student.objects.filter(id=id)
            Mark_obj = Marks.objects.filter(student_id= id)

            st_obj.delete()
            Mark_obj.delete()

        return Response({
            "Status":True,
            "Message":"data Deleted "
        })














# {
#     "name" : "Raju",
#     "phone" : "123456789",
#     "physics" : 50,
#     "chemistry" : 40,
#     "Maths" : 90,
#     "Botany" : 34,
#     "Zoology" : 45,
#     "English" : 49
# }
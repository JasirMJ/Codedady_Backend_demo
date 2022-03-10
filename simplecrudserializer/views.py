
import json
from urllib import response
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Student
from .Serializers import *
from students.Checking_Fun import Checking


# Create your views here.
class Studentsser(ListAPIView):
    serializer_class = StudentSerializer

    def post(self,request):
        id =self.request.POST.get("id","")
        if id:
            student_to_modify = Student.objects.filter(id=id)
           

            if student_to_modify.count():
                stdent_to_modify = student_to_modify.first()
               
                student_create = StudentSerializer(stdent_to_modify,data=self.request.data,partial=True)
              
                msg = "Updated Succesfully"

            else:
                return Response({
                    "status" : False,
                    "Message" : "No Data Found"
                })

        else:
            student_create = StudentSerializer(data=self.request.data,partial=True)         
            msg = "Created succesfully"

        student_create.is_valid(raise_exception=True)
        student_create.save()
     

        return Response({
            "status" : True,
            "Message" : msg
        })

    def get_queryset(self):
        s = Student.objects.all()
        id = self.request.POST.get("id","")
        name = self.request.POST.get("name","")
        if id:
            s = s.filter(id=id)
       
        if name:
            s = s.filter(name__icontains = name )

        return s

    # def delete(self,request):
    #     id = self.request.POST.get("id","")
        
    #     if Student.objects.filter(id=id):
    #         Student.objects.get(id=id).delete()
    #         return Response({

    #             "status" : True,
    #             "Message" : "Deleted Succesfully"
    #         })
    #     else:
    #         return Response({

    #             "status" : False,
    #             "Message" : "ID Does not Exist"
    #         })

    def delete(self,request):
        id = self.request.POST.get("id","[]")
        try:
            id = json.loads(id)
            Student.objects.filter(id__in = id).delete()
            return Response({
                "status" : True,
                "Message" : "Deleted Succesfully"
            })
        except:
            return Response({
                "Status" : False,
                "Message" : "Please Give in a list format"
            })
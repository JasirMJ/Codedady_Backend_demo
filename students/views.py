from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import *
from .Checking_Fun import Checking
# Create your views here.

class StudentAPI(ListAPIView):

    def post(self,request):

        st_id = self.request.POST.get("id","")
        name = self.request.POST.get("name","")
        phone = self.request.POST.get("phone","")
        
        physics = self.request.POST.get("physics",0)
        chemistry = self.request.POST.get("chemistry",0)
        Maths = self.request.POST.get("Maths",0)
        Botany = self.request.POST.get("Botany",0)
        Zoology = self.request.POST.get("Zoology",0)
        English = self.request.POST.get("English",0)
        Semester = self.request.POST.get("semester","")

        Total = int(physics) + int(chemistry) + int(Maths) + int(Botany) + int(Zoology) + int(English)
   
        if st_id == "":
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
        else:
           
            if Semester == "":

                return Response({
                    "status" : False,
                    "Message" : "Provide A Valid Semester"
                })

            else:
                sem = []
                stdts = []
                stids=student.objects.filter(id = st_id)
                for x in stids:
                    stdts.append(x.id)
                datas = Marks.objects.filter(student_id = st_id)
                for x in datas:
                    sem.append(x.Semester)

                if len(stdts) == 0:
                    return Response({
                        "status" : False,
                        "Message" : "The Student ID Does Not Exist"
                    })

                elif Semester in sem:
                    return Response({
                        "Status" : False,
                        "Message" : "This Semester Alrady Added"
                    })
               
                else:
                    mark_obj = Marks.objects.create(student_id = st_id,physics = physics,chemistry=chemistry,Maths=Maths,Botany=Botany,Zoology=Zoology,English=English,Total=Total,Semester=Semester)
                    return Response({
                        "status" : True,
                        "Message" : "Succesfully Created Semester Mark"
                    })

    
    def get(self,request):

        id = self.request.POST.get("id","")
        
        stdts = []
        if id != "":
            stids=student.objects.filter(id = id)
            for x in stids:
                stdts.append(x.id)    
        else:
            pass

        if id == "":          
           
            st_obj = student.objects.all()
            mark_obj = Marks.objects.all()
            data = []
            sub = []
          
            for x in st_obj:
                sub = []
                id = x.id
                data.append({
                    'name' : x.name,
                    'id'  : x.id,
                    'Phone' : x.phone,
                    'Subject' : sub
                })
                for y in mark_obj:
                    if y.student_id == id:
                        sub.append({
                            'physics' : y.physics,
                            'chemistry' : y.chemistry,
                            'Maths' : y.Maths,
                            'Botany' : y.Botany,
                            'Zoology' : y.Zoology,
                            'English' : y.English,
                            'Total' : y.Total,
                            'Semester ' : y.Semester
                        })
            
            return Response({
                'status' : True,
                'Result Data' : data
            })     
        elif len(stdts) == 0:
            return Response({
                'status' : False,
                "Message" : "The Stdent ID Does Not Exist "
            })           
        else:
            st_obj = student.objects.filter(id = id)
            mark_obj = Marks.objects.filter(student_id = id)
            data = []
            sub = []
            for x in st_obj:
                sub = []
                id = x.id
                data.append({
                    'name' : x.name,
                    'id'  : x.id,
                    'Phone' : x.phone,
                    'Subject' : sub
                })
                for y in mark_obj:
                    if y.student_id == id:
                        sub.append({
                            'physics' : y.physics,
                            'chemistry' : y.chemistry,
                            'Maths' : y.Maths,
                            'Botany' : y.Botany,
                            'Zoology' : y.Zoology,
                            'English' : y.English,
                            'Total' : y.Total,
                            'Semester ' : y.Semester
                        })
            return Response({
                'status' : True,
                'Data' : data
            })
    
    def put(self,request):
        
        id = self.request.POST.get("id","")
        Semester =  self.request.POST.get("semester","")

        name = self.request.POST.get("name","")
        phone = self.request.POST.get("phone","")
        
        physics = self.request.POST.get("physics","")
        chemistry = self.request.POST.get("chemistry","")
        Maths = self.request.POST.get("Maths","")
        Botany = self.request.POST.get("Botany","")
        Zoology = self.request.POST.get("Zoology","")
        English = self.request.POST.get("English","")

        sem = []
        stdts = []
        stids=student.objects.filter(id = id)
        for x in stids:
            stdts.append(x.id)
        datas = Marks.objects.filter(student_id = id).filter(Semester=Semester)
        for x in datas:
            sem.append(x.Semester)
                  
        if id == "" or name == "" or phone == "" or physics == "" or chemistry == "" or Maths == "" or Botany == "" or Zoology == "" or English == "" or Semester == "":
            return Response({
                "status" : False,
                "Message" :  "PLease Fill Your All Field"
            })
        elif len(stdts) == 0:
            return Response({
                "Status" : False,
                "Message" : "The Student ID is Does Not Match"
            })
        elif len(sem) == 0:
            return Response({
                "Status" : False,
                "Message" : "The Semester Does Not Exist"
            })
        else:
            Total = int(physics) + int(chemistry) + int(Maths) + int(Botany) + int(Zoology) + int(English)
            st_obj = student.objects.get(id = id)
            mark_obj = Marks.objects.filter(student_id = id).get(Semester=Semester)
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
        stdts = []
        if id != "":
            stids=student.objects.filter(id = id)
            for x in stids:
                stdts.append(x.id)    
        else:
            pass

        if id == "":
            return Response({
                "status" : False,
                "Message" :  "PLease Fill Your Id"
            })
        elif len(stdts) == 0:
            return Response({
                "status" : False,
                "Message" : "The User With This ID Does Not Exist"
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
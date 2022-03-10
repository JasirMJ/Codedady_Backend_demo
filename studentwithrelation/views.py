from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework.generics import ListAPIView 
from students.Checking_Fun import Checking
# Create your views here.


class StudentAPINew(ListAPIView):
    def post(self,request):
        mandatory = ['prof_image','name','physics_mrk','chemistry_mrk','maths_mrk','botany_mrk','zoology_mrk','english_mrk','semester']
        data = Checking(self.request.data,mandatory)
        
        if data == True:

            st_id = self.request.POST.get("id","")
            prof_image = self.request.FILES.get("prof_image","")
            name = self.request.POST.get("name","")
        
            physics_mrk = self.request.POST.get("physics_mrk",0)
            chemistry_mrk = self.request.POST.get("chemistry_mrk",0)
            maths_mrk = self.request.POST.get("maths_mrk",0)
            botany_mrk = self.request.POST.get("botany_mrk",0)
            zoology_mrk = self.request.POST.get("zoology_mrk",0)
            english_mrk = self.request.POST.get("english_mrk",0)
            Semester = self.request.POST.get("semester","")
            st_class = self.request.POST.get("st_class","")

            total = int(physics_mrk) + int(chemistry_mrk) + int(maths_mrk) + int(botany_mrk) + int(zoology_mrk) + int(english_mrk)
            if prof_image == "":
                return Response({
                    "status" : False,
                    "Message" : "The Pofile Image was Incorrect"
                })
            if st_id == "":
                
                st_obj = Student.objects.create(name=name,prof_image=prof_image)
                mark_obj = Marks.objects.create(student_id = Student.objects.get(id=st_obj.id),physics_mrk = physics_mrk,chemistry_mrk=chemistry_mrk,maths_mrk=maths_mrk,botany_mrk=botany_mrk,zoology_mrk=zoology_mrk,english_mrk=english_mrk,total=total,semester=Semester)
        
                return Response({
                    "status" : True,
                    "Message" : "Succesfully Created User"
                })
            else:
                sem = []
                stdts = []
                stids=Student.objects.filter(id = st_id)
                for x in stids:
                    stdts.append(x.id)
                datas = Marks.objects.filter(student_id = st_id)
                for x in datas:
                    sem.append(x.semester)

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
                    st =Student.objects.get(id = st_id)
                    # for x in st:
                    #     print(x)
                    mark_obj = Marks.objects.create(student_id = st,physics_mrk = physics_mrk,chemistry_mrk=chemistry_mrk,maths_mrk=maths_mrk,botany_mrk=botany_mrk,zoology_mrk=zoology_mrk,english_mrk=english_mrk,total=total,semester=Semester)
                    
                    return Response({
                        "status" : True,
                        "Message" : "Succesfully Created Semester Mark"
                    })
        else:
            return Response({
                "Status" : False,
                "Message" : data
            })

    def get(self,request):

        id = self.request.POST.get("id","")
        
        stdts = []
        if id != "":
            stids=Student.objects.filter(id = id)
            for x in stids:
                stdts.append(x.id)    
        else:
            pass

        if id == "":          
           
            st_obj = Student.objects.all()
            mark_obj = Marks.objects.all()
            data = []
            sub = []
          
            for x in st_obj:
                sub = []
                id = x.id
                data.append({
                    'name' : x.name,
                    'id'  : x.id,
                    'Image' : x.prof_image.url,
                    'Subject' : sub
                })
                for y in mark_obj:
                    if y.student_id.id == id:
                        sub.append({
                            'physics' : y.physics_mrk,
                            'chemistry' : y.chemistry_mrk,
                            'Maths' : y.maths_mrk,
                            'Botany' : y.botany_mrk,
                            'Zoology' : y.zoology_mrk,
                            'English' : y.english_mrk,
                            'Total' : y.total,
                            'Semester ' : y.semester
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
            st_obj = Student.objects.filter(id = id)
            mark_obj = Marks.objects.filter(student_id = id)
            data = []
            sub = []
            for x in st_obj:
                sub = []
                id = x.id
                data.append({
                    'name' : x.name,
                    'id'  : x.id,
                    'Image' : x.prof_image.url,
                    'Subject' : sub
                })
                for y in mark_obj:
                    if y.student_id.id == id:
                        sub.append({
                            'physics' : y.physics_mrk,
                            'chemistry' : y.chemistry_mrk,
                            'Maths' : y.maths_mrk,
                            'Botany' : y.botany_mrk,
                            'Zoology' : y.zoology_mrk,
                            'English' : y.english_mrk,
                            'Total' : y.total,
                            'Semester ' : y.semester
                        })
            return Response({
                'status' : True,
                'Data' : data
            })

    def put(self,request):

        mandatory = ['id','prof_image','name','physics_mrk','chemistry_mrk','maths_mrk','botany_mrk','zoology_mrk','english_mrk','semester']
        data = Checking(self.request.data,mandatory)
        if data == True:
            id = self.request.POST.get("id","")
            prof_image = self.request.FILES.get("prof_image","")
            name = self.request.POST.get("name","")
        
            physics_mrk = self.request.POST.get("physics_mrk",0)
            chemistry_mrk = self.request.POST.get("chemistry_mrk",0)
            maths_mrk = self.request.POST.get("maths_mrk",0)
            botany_mrk = self.request.POST.get("botany_mrk",0)
            zoology_mrk = self.request.POST.get("zoology_mrk",0)
            english_mrk = self.request.POST.get("english_mrk",0)
            Semester = self.request.POST.get("semester","")
            total = int(physics_mrk) + int(chemistry_mrk) + int(maths_mrk) + int(botany_mrk) + int(zoology_mrk) + int(english_mrk)

            sem = []
            stdts = []
            stids=Student.objects.filter(id = id)
            for x in stids:
                stdts.append(x.id)
            datas = Marks.objects.filter(student_id = id).filter(semester=Semester)
            for x in datas:
                sem.append(x.semester)
            if prof_image == "":
                return Response({
                    "status" : False,
                    "Message" : "The Pofile Image was Incorrect"
                })
            if len(stdts) == 0:
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
                total = int(physics_mrk) + int(chemistry_mrk) + int(maths_mrk) + int(botany_mrk) + int(zoology_mrk) + int(english_mrk)
                st_obj = Student.objects.get(id = id)
                mark_obj = Marks.objects.filter(student_id = id).get(semester=Semester)
                st_obj.name  = name
                st_obj.prof_image = prof_image
                mark_obj.physics_mrk = physics_mrk
                mark_obj.chemistry_mrk = chemistry_mrk
                mark_obj.maths_mrk = maths_mrk
                mark_obj.botany_mrk = botany_mrk
                mark_obj.zoology_mrk = zoology_mrk
                mark_obj.english_mrk = english_mrk
                mark_obj.total = total
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
            stids=Student.objects.filter(id = id)
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
            st_obj = Student.objects.filter(id=id)
            Mark_obj = Marks.objects.filter(student_id= id)

            st_obj.delete()
            Mark_obj.delete()

            return Response({
                "Status":True,
                "Message":"data Deleted "
            })
       
       
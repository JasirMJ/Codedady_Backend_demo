from email.policy import default
from queue import Empty
from typing import List
from unicodedata import name
from urllib import response
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from studentsapp.checking import Checking
from .models import *

# Create your views here.
class StudentAPI(ListAPIView):
    def post(self,request):
        mandatory=['name']
        data=Checking(self.request.data,mandatory)
        if data==True:  
            try:  
                name=self.request.POST.get('name',"default")
                # std_obj=StudentModel.objects.all()
                # if name in std_obj:
                #     return Response({
                #         "message":"name already exist"
                #     })
                # else:
                std_obj=StudentModel.objects.create(name=name)
                return Response({
                    "Status":True,
                    "Message":"Saved Successfully",
                    "Data":self.request.data,
                    })
            
                # second table
                # std_obj=StudentModel.objects.all()
                # id=std_obj.id
                # print("id",id)
                # idd=id
                # english=self.request.POST.get('english',0.0)
                # physics=self.request.POST.get('physics',0.0)
                # chemistry=self.request.POST.get('chemistry',0.0)
                # maths=self.request.POST.get('maths',0.0)
                # biology=self.request.POST.get('biology',0.0)
                # arabic=self.request.POST.get('arabic',0.0)
                # subject=self.request.POST.get('subject',"default")
                # mark=self.request.POST.get('mark',0.0)
                # sub_obj=SubjectModel.objects.create(stu_id=std_obj.id,subject=subject,mark=mark)          
                # except Exception as e:
                #     msg = "Excepction occured "+str(e)
                #     return Response({
                #         "Status":False,
                #         "Message":msg,
                #     })
            
            except Exception as e:
                msg = "Excepction occured "+str(e)
                return Response({
                    "Status":False,
                    "Message":msg,
                })
        else:
            return Response({
                "status":False,
                "message":data,
            })
            
    def get(self,request):
        try:
            id = request.POST.get("id",0)
            stu_obj=StudentModel.objects.all()
            print("stuobj",stu_obj)
            try:
                for x in stu_obj:
                    print("name in get stuobj",x.name)
                    print("id of student",x.id)
                    student_id=x.id
                    print("studentid",student_id)
                    print("givenid",id)
                    # try:
                    if int(id)==int(student_id):
                        print("okkk")
                        stu_obj=StudentModel.objects.filter(id=id)
                        # sub_obj=SubjectModel.objects.filter(stu_id=id)
                    # elif id!=student_id:
                    #     return Response({
                    #         "message":"entered id not in list"
                    #     })
                    else:
                        pass
                        # stu_obj=StudentModel.objects.all()
                        # sub_obj=SubjectModel.objects.all()
                    # print("idname",sub_.name)
                    data=[]
                    print("stuobj",stu_obj)
                    for x in stu_obj:
                        data.append(
                            {
                                "id":x.id,
                                "name":x.name,
                            }
                        )
                # for (x,y) in zip(sub_id,stu_obj):
                    
                # for  x in sub_id:
                #     data.append(
                #         {
                #             "name":x.name,
                #         })
                # --------------------------------------------------
                # for y in sub_obj:
                #     data.append(
                #         {                       
                #             "student_id":y.stu_id,
                #             "subject":y.subject,
                #             "mark":y.mark,
                #             # "stu_id":y.stu_id,
                #             # "english":y.english,
                #             # "maths":y.maths,
                #             # "physics":y.physics,
                #             # "chemistry":y.chemistry,
                #             # "biology":y.biology,
                #             # "arabic":y.arabic,
                            
                #         }
                #     )
                if len(data)==0:
                    return Response({
                        "status":True,
                        "Data":data,
                        "msg":"data is empty"
                    })
                else:
                    sub_id=StudentModel.objects.get(id=id)
                    namecheck=sub_id.name
                    print("iddd",namecheck)
                    return Response({
                    "name":namecheck,
                    "subject":data,
                })
            except:
                data=[]
                print("stuobj",stu_obj)
                for x in stu_obj:
                    data.append({
                            "id":x.id,
                            "name":x.name,
                        })
                return Response({
                    "status":"id not in list",
                    "the datas in list":data,

                })
        except Exception as e:
            msg = "Excepction occured "+str(e)
            return Response({
                "Status":False,
                "Message":msg,
            })
            
                 
    def put(self,request): 
        mandatory=['id','name']
        data=Checking(self.request.data,mandatory)
        if data==True:  
            try:
                id=request.POST.get("id","")
                name=request.POST.get("name","")

                # english=self.request.POST.get('english',0.0)
                # physics=self.request.POST.get('physics',0.0)
                # chemistry=self.request.POST.get('chemistry',0.0)
                # maths=self.request.POST.get('maths',0.0)
                # biology=self.request.POST.get('biology',0.0)
                # arabic=self.request.POST.get('arabic',0.0)
                # subject=self.request.POST.get('subject',"default")
                # mark=self.request.POST.get('mark',0.0)             
                # if  id=="" or name=="" or english=="" or physics=="" or chemistry=="" or maths=="" or biology=="" or arabic=="":
                if id==name=="":
                    return Response({
                        "status":False,
                        "msg":"some Fields are empty"
                    })  
                    
                else:
                    stu_obj=StudentModel.objects.get(id=id)
                    # sub_obj=SubjectModel.objects.get(stu_id=id)
                    stu_obj.name = name
                    # sub_obj.english = english
                    # sub_obj.physics = physics
                    # sub_obj.chemistry = chemistry
                    # sub_obj.maths = maths
                    # sub_obj.biology = biology
                    # sub_obj.arabic = arabic
                    stu_obj.save()
                    # sub_obj.save()

                    return Response({
                        "status":True,
                        "message":"Saved Successfully ",
                        "Data":self.request.data,
                    })
                # id =  request.POST.get("id")
                # name=request.POST.get("name")

                # english=self.request.POST.get('english')
                # physics=self.request.POST.get('physics')
                # chemistry=self.request.POST.get('chemistry')
                # maths=self.request.POST.get('maths')
                # biology=self.request.POST.get('biology')
                # arabic=self.request.POST.get('arabic') 

                # if id=="" or name=="" or english=="" or physics=="" or chemistry=="" or maths=="" or biology=="" or arabic=="":
                #     return Response({
                #         "id":"Failed"
                #     })
                # else:
                #       return Response({
                #         "id":id
                #     })
            except Exception as e:
                msg = "Excepction occured "+str(e)
                return Response({
                    "Status":False,
                    "Message":msg,
                })
        else:
            return Response({
                "status":False,
                "message":data,
            })
                
    def delete(self,request):
        try:
            id=request.POST.get("id")
            stu_obj=StudentModel.objects.get(id=id)
            sub_obj=SubjectModel.objects.get(stu_id=id)
            stu_obj.delete()
            sub_obj.delete()
            return Response({
                "status":True,
                "message":"deleted successfully",
            })

        except Exception as e:
            msg = "Excepction occured "+str(e)
            return Response({
                "Status":False,
                "Message":msg,
            })

class SubjectAPI(ListAPIView):
    def post(self,request):
        mandatory=['id','subject','mark']
        data=Checking(self.request.data,mandatory)
        if data==True:

            try:
                stu_id=self.request.POST.get('id',0)
                subject=self.request.POST.get('subject',"default")
                mark=self.request.POST.get('mark',0.0)
                sub_obj=SubjectModel.objects.filter(stu_id=stu_id)
                sublist=[]
                for x in sub_obj:
                    sublist.append(x.subject)
                    print("idsss",x.subject)
                    

                if subject in sublist:
                    return Response({
                        "message":subject +" already exist"
                    })
                else:

                    sub_obj=SubjectModel.objects.create(stu_id=stu_id,subject=subject,mark=mark)
                        
                    return Response({
                        "Status":True,
                        "Message":"Saved Successfully",
                        "Data":self.request.data,
                    })
                # except Exception as e:
                #     msg = "Excepction occured "+str(e)
                #     return Response({
                #         "Status":False,
                #         "Message":msg,
                    # })
                    # if sub_id.name in data:
                    # return Response({
                    #     "message":"name already exist"
                    # })
            except Exception as e:
                msg = "Excepction occured "+str(e)
                return Response({
                    "Status":False,
                    "Message":msg,
                })
        else:
            return Response({
                "status":False,
                "message":data,
            })
            
    def get(self,request):
        total_mark=0       
        id = request.POST.get("id","")
        print("id befor",id)
        stu_obj=StudentModel.objects.all()
        print("stuobj",stu_obj)
        studentlist=[]
        for x in stu_obj:
            studentlist.append(x.id)
            
        print("stulist",studentlist)
        try:
            if int(id) in studentlist:
                print(" print id ")
                # stu_obj=StudentModel.objects.filter(id=id)
                sub_obj=SubjectModel.objects.filter(stu_id=id)
            
            else:
                print("all print")
                sub_obj=SubjectModel.objects.all()
                
            
            # print("idname",sub_.name)
            data=[]
            for y in sub_obj:
                data.append({      
                        "student_id":y.stu_id,
                        "subject":y.subject,
                        "mark":y.mark,       
                    })
            print("after for loop")
            if len(data)==0:
                print("in length of data==0")
                return Response({
                    "status":True,
                    "Data":data,
                    "msg":"id not in list"
                })
            else:
                print("length of data!=0")
               
                if int(id) in studentlist:

                    sub_obj=SubjectModel.objects.filter(stu_id=id)
                    for x in sub_obj:
                        total_mark=total_mark + int(x.mark)


                    stu_id=StudentModel.objects.get(id=id)
                    namecheck=stu_id.name
                    print("iddd",namecheck)
                    return Response({
                        "name":namecheck,
                        "subject":data,
                        "total_mark":total_mark,
                    })
                else:
                    return Response({
                        "subject":data,
                        
                    })
        except :
            sub_obj=SubjectModel.objects.all()
            data=[]
            for y in sub_obj:
                data.append({      
                        "student_id":y.stu_id,
                        "subject":y.subject,
                        "mark":y.mark,       
                    })
            return Response({
                "Status":False,
                "subject":data,
            })
       
    def put(self,request): 
        mandatory=['id','subject','mark']
        data=Checking(self.request.data,mandatory)
        if data==True:
            try:
                stu_id=request.POST.get("id","")

                subject=self.request.POST.get('subject',"default")
                mark=self.request.POST.get('mark',0.0)
            
                stuids=[]
                stu_obj=StudentModel.objects.all()
                for x in stu_obj:
                    stuids.append(x.id)
                print("list",stuids)
                if int(stu_id) in stuids:
                
            
                    # if stu_id==subject==mark=="":
                    if not all([stu_id,subject,mark]):
                        return Response({
                            "status":False,
                            "msg":"some Fields are empty"
                        })  
                        
                    else:
                        # stu_obj=StudentModel.objects.get(id=id)
                        sub_obj=SubjectModel.objects.get(stu_id=stu_id,subject=subject)

                        sub_obj.stu_id = stu_id
                        sub_obj.subject = subject
                        sub_obj.mark = mark
                    
                        # stu_obj.save()
                        sub_obj.save()

                        return Response({
                            "status":True,
                            "message":"Saved Successfully ",
                            "Data":self.request.data,
                
                        })
                else:
                    return Response({
                        "message":"given id not in list"
                    })  
            
            except Exception as e:
                msg = "Excepction occured "+str(e)
                return Response({
                    "Status":False,
                    "Message":msg,
                })
        else:
            return Response({
                "status":False,
                "message":data,
            })
    def delete(self,request):
        try:
            id=request.POST.get("id")
            subject=request.POST.get("subject")
            # stu_obj=StudentModel.objects.get(id=id)
            sub_obj=SubjectModel.objects.get(stu_id=id,subject=subject)
            # stu_obj.delete()
            sub_obj.delete()
            return Response({
                "status":True,
                "message":"deleted successfully",
            })

        except Exception as e:
            msg = "Excepction occured "+str(e)
            return Response({
                "Status":False,
                "Message":msg,
            })

       
               



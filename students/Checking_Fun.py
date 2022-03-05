from rest_framework.response import Response
from .models import *
def Checking(data):
    
    try:
        st_id = data["id"]
        name = data["name"]
        phone = data["phone"]        
        physics = data["physics"]
        chemistry = data["chemistry"]
        Maths = data["Maths"]
        Botany = data["Botany"]
        Zoology = data["Zoology"]
        English = data["English"]
        Semester = data["semester"]
        
        return True
    except Exception as e:
       
        return e

    


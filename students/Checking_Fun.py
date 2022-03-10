from rest_framework.response import Response
from .models import *

def Checking(data,mandatory):


    # mandatory = ['name','phone','semester']  
    not_present = []
    for x in mandatory:
        if x not in data:
            not_present.append(x)
            return (f"{x} Is Not Presnet")
        else:
            if data[x] == "":
                not_present.append(x)
                return (f"{x} Cannot Use as null" )
            else:
                pass

    if len(not_present) == 0:
        return True
    else:
        pass
     
    # if "name" in data:
    #     print("data is here")
    #     return data["name"]
    # else:
    #     print("no data")
    #     return "no data"
   
    # array = ['name' , 'phone' , 'physics']
    # for x in array:
    #     if data['x']=="":
    #         print(f"{data['x']} can not be empty")
    
   


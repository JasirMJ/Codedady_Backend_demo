def Checking(data,    mandatory ):
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
    if len(not_present)==0:
        return True
# mandatory=[{""}]
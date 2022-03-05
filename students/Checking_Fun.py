from asyncio.windows_events import NULL


def Checking(data):
    try:
        if data['id'] == "" or data['name'] == "" or data["phone"] == "" or data["physics"] == "" or data["chemistry"] == "" or data["Maths"] == "" or data["Botany"] == "" or data["Zoology"] == "" or data["English"] == "" :
            return False
    except:
        return NULL
    # print(data['id'])


from celery import shared_task

@shared_task
def add(x, y):
    res = str(x+y)
    print("x+y ",x+y)
    f = open("demofile2.txt", "a")
    f.write("Now the file has more content!")

    print("file created ",f.close())
    return x + y
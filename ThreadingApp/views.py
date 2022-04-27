from django.shortcuts import render
import ctypes
import sys
import time
import threading
from threading import Thread

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.response import Response


class TestThread(ListAPIView):

    def get(self,request):
        stop=self.request.GET.get("stop","false")
        name=self.request.GET.get("name","")
        stop_thread_name=self.request.GET.get("stop_thread_name","")
        counter=self.request.GET.get("counter","")
        duration=self.request.GET.get("duration","")
        if duration:
            duration_thread=thread_with_trace("duration",int(duration))
            duration_thread.daemon = True
            duration_thread.start()

        if name and counter:
            t1 = thread_with_trace(name,int(counter))
            t1.daemon = True
            t1.start()

        print("main thread is ",threading.main_thread())
        if stop == "true":
            print("stop request",stop_thread_name)
            # t1.kill()
            for thread in threading.enumerate():
                print("current threads are-->",thread.name)
                if thread.name==stop_thread_name:
                    print("going to stop -->", thread.name)
                    thread.raise_exception()

        return Response({
            "Status":True
        })

class thread_with_trace(threading.Thread):
    def __init__(self, name,n):
        threading.Thread.__init__(self)
        self.name = name
        self.n = n

    def run(self):
        try:
            n=self.n
            while n >= 0:
                if n==0:
                    print("Run Status change funciton here")
                    # for thread in threading.enumerate():
                    #     print("threads are ****",thread.name)
                    #
                    #     if thread.name == "MainThread":
                    #         print("main thread",thread)
                    #     elif thread.name == "Thread-1":
                    #         print("Thread-1")
                    #     elif thread.name == "django-main-thread":
                    #         print("django-main-thread")
                    #     else:
                    #
                    #         print("else", thread.name,)
                    #         thread.raise_exception()

                print("seconds-->", n,", thread name--->",self.name)
                n -= 1
                time.sleep(1)
        finally:

            print('ended')

    def get_id(self):

        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id

    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
                                                         ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')

    # def __init__(self,name, *args, **keywords):
    #     threading.Thread.__init__(self, *args, **keywords)
    #     self.killed = False
    #     print(keywords)
    #
    #     self.name=name
    #
    # def start(self):
    #     self.__run_backup = self.run
    #     self.run = self.__run
    #     threading.Thread.start(self)
    #
    # def __run(self):
    #     sys.settrace(self.globaltrace)
    #     self.__run_backup()
    #     self.run = self.__run_backup
    #
    # def globaltrace(self, frame, event, arg):
    #     if event == 'call':
    #         return self.localtrace
    #     else:
    #         return None
    #
    # def localtrace(self, frame, event, arg):
    #     if self.killed:
    #         if event == 'line':
    #             raise SystemExit()
    #     return self.localtrace

    def kill(self):
        self.killed = True

    def isAlive(self):
        self.isAlive = True



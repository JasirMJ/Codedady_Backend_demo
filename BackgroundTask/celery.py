from __future__ import absolute_import
import os
from celery import Celery

from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Codedady_Demo.settings')
app = Celery('Codedady_Demo',
        include=['BackgroundTask.tasks'],
             )

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))



# from celery import shared_task
#
# @shared_task
# def add(x, y):
#     res = str(x+y)
#     print("x+y ",x+y)
#     # f = open("demofile2.txt", "a")
#     # f.write("Now the file has more content!")
#     # f.close()
#     return x + y
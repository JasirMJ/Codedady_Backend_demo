from django.urls import path
from  simplecrudserializer import views
from .views import Studentsser

urlpatterns = [
    # path('datas/',views.Studentsser.as_view())
    path('datas/',Studentsser.as_view())
]
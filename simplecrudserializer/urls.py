from django.urls import path

from simplecrudserializer import views

urlpatterns = [
    path('',views.ProductSAPI.as_view()),
    # path('asd/',views.ProductSAPI.as_view()),

]
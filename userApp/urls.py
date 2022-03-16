from django.urls import path

from userApp import views

urlpatterns = [
    path('',views.UserAPI.as_view()),
    path('whoami/',views.WhoAmI.as_view()),
    path('login/',views.LoginView.as_view()),
]
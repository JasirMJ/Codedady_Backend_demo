from django.contrib.auth.hashers import make_password
from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from userApp.models import UserDetails
from userApp.serializers import UserSerializer
from rest_framework.authtoken.models import Token

class UserAPI(ListAPIView):
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)


    def get_queryset(self):
        qs = UserDetails.objects.all()
        return qs.order_by('-id')

    def post(self, request):
        user_obj = ""
        print("Receved User data ",self.request.data)

        try:
            id = self.request.POST.get("id", "")
            if id:
                user_qs = UserDetails.objects.filter(id=id)
                serializer = UserSerializer(user_qs.first(),data=request.data,partial=True)
                serializer.is_valid(raise_exception=True)

                password = self.request.POST.get('password','')
                if password :
                    msg="User details and password updated"
                    user_obj = serializer.save(password=make_password(password))
                else:
                    msg="User details updated"
                    user_obj = serializer.save()
            else:
                print("Adding new UserDetails")
                serializer = UserSerializer(data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                msg = "Data saved"
                msg = "Created New User"
                user_obj = serializer.save(password=make_password(self.request.data['mobile']))


            # token, created = Token.objects.get_or_create(user=user_obj)
            # return ResponseFunction(1, msg,{})
            return Response({
                "Status":True,
                "Message":"User Created"
            })

        except Exception as e:
            print(f"Excepction occured {e}")

            if user_obj:
                user_obj.delete()

            return  Response({
                "Status":False,
                "Message":f"Excepction occured {e}"
            })

class WhoAmI(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self,request):

        return Response({
            "Status":1,
            "Data":self.request.user.username
        })


class LoginView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        # print(serializer)
        try:
            test = serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']


            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "STATUS":True,
                'token': "Token "+token.key,
                'user_id': user.pk,
                'username': user.username,
                'is_superuser':user.is_superuser,
            })
        except Exception as e:
            return Response({
                "STATUS":False,
                "MESSAGE":"Incorrect Username or Password",
                "excepction":str(e),
            })




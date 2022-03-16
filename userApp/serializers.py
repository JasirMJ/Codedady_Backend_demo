from django.contrib.auth.models import User
from rest_framework import serializers

from userApp.models import UserDetails


#
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = "__all__"

from rest_framework import serializers
from .models import User

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','phone_number','name','natianal_id',)
        model = User


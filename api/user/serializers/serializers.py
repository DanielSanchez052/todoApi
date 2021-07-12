import django.contrib.auth.password_validation as validators
from rest_framework import serializers
from api.user.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )
    class Meta:
        model = User
        fields = ['username','password','email','name','last_name','image']
    
    def validate_password(self, data):
            validators.validate_password(password=data, user=User)
            return data

    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
    
    def to_representation(self,instance):
        return {
            'username': instance.username,
            'email': instance.email,
            'name':instance.name,
            'last_name': instance.last_name,
            'image': instance.image,
        }

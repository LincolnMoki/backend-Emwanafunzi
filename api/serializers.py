from rest_framework import serializers
from .models import Category, Product, Profile
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = User
        fields = ['email', 'username', 'password','password2','role']
        extra_kwargs = {
            'password': {'write_only':True}
        }
    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            role = self.validated_data['role']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password':'Passwords must match'})
        user.set_password(password)
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'role']

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = (
            'id',
            'title'
        )
        model = Category 

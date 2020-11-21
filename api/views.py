from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer,  CategorySerializer, ProductSerializer, RegistrationSerializer, ProfileSerializer
from .models import User, Profile, Category, Product
from django.contrib import auth
from rest_framework import status
from django.conf import settings
from .permissions import IsCompanyAdmin, IsNormalUser
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from urllib import request
from django.http  import HttpResponse
import jwt
# Create your views here.



class RegisterView(GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
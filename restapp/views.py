from contextvars import Token
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.middleware.csrf import get_token
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .serializer import *
#admin register





@api_view(['POST'])
def admin_login(request):
    data = request.data

    if 'email' not in data or 'password' not in data:
        return Response("Username and password required", status=status.HTTP_400_BAD_REQUEST)
    
    email = data['email']
    password = data['password']
    print(email,password)
    
    # Authenticate the user
    user = User.objects.filter(email=email).first()
    print(user)

    if user is not None:
        # Check if the user already has a token
       
        id=user.id
        username=user.username
        password=user.password
        
        # Return token as part of the response
        return Response({'message': 'Login successful','email':email,'password':password,'id':id,'username':username}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['POST'])
def addapp(request):
    data=request.data
    serializer=AppcollectionsSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response('Added sucessfully')
    
@api_view(['DELETE'])
def deleteapp(request,id):
        id=id
        app=Appcollections.objects.filter(id=id).delete()
    
        return Response('Added sucessfully')
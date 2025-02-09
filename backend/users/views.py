from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import LoginSerializer
import json

# Create your views here.

def index(request):
    return redirect('/users/login')

def login_page(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            user = serializer.validated_data
            login(request, user)
            return JsonResponse({'message': 'Login successful'}, status=200)
        else:
            return render(request, 'index.html', {'error':"Invalid credentials"})
    return render(request, 'index.html')

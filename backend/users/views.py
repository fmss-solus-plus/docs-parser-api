from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .serializers import LoginSerializer
from drf_spectacular.views import SpectacularSwaggerView

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


@login_required
def docs_page(request):
    return SpectacularSwaggerView.as_view(url_name='schema')(request)
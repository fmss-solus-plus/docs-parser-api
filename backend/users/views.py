from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from drf_spectacular.views import SpectacularSwaggerView

from .serializers import LoginSerializer
from backend.status_code import STATUS_CODES, STATUS_MESSAGES

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
            return JsonResponse({'message': f'{STATUS_MESSAGES["success"]["LOGIN_SUCCESSFUL"]}'}, 
                            status=STATUS_CODES["success"][200])
        else:
            return JsonResponse({'message': f'{STATUS_MESSAGES["errors"]["INVALID_CREDENTIALS"]}'}, 
                            status=STATUS_CODES["errors"][401])
    return render(request, 'index.html')


@login_required
def docs_page(request):
    return SpectacularSwaggerView.as_view(url_name='schema')(request)
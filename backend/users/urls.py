from django.urls import path
from .views import login_page, docs_page
from drf_spectacular.views import SpectacularAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('schema/', (SpectacularAPIView.as_view()), name='schema'),
    path('docs/', docs_page, name='swagger-ui'),
    
    path('token/', TokenObtainPairView.as_view(), name='get_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),

    path("login/", login_page, name='login_page')    
]
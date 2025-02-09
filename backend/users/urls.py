from django.urls import path
from .views import login_page, docs_page
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('schema/', (SpectacularAPIView.as_view()), name='schema'),
    path('docs/', docs_page, name='swagger-ui'),

    path("login/", login_page, name='login_page')
]
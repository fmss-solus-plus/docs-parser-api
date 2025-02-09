from django.urls import path
from .views import login_page
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('schema/', (SpectacularAPIView.as_view()), name='schema'),
    path('docs/', (SpectacularSwaggerView.as_view(url_name='schema')), name='swagger-ui'),

    path("login/", login_page, name='login_page')
]
from django.urls import path,include
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='jwt-login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),

    path('api/get/', TestView.as_view(), name='test'),
]

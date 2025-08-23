from django.urls import path
from rest_framework_simplejwt.views import  TokenRefreshView
from .views import RegisterView, TokenAcsessView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenAcsessView.as_view(), name='token_access'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
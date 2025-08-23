from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import CreateAPIView
from .serializers import (
    UserCreateSerializer, UserSerializer
    )

from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class TokenAcsessView(TokenObtainPairView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, allow_blank=True)
    confirm_password = serializers.CharField(write_only=True)
    token= serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ( 'first_name', 'last_name','region',
                'district','school','class_number',
                'class_sign','email','password',
                'confirm_password','token',
        )

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)
        user = User.objects.create_user(**validated_data)
        return user
    
    def get_token(self, user ):
        from rest_framework_simplejwt.tokens import RefreshToken
        token = RefreshToken.for_user(user)
        token['email'] = user.email
        return {
            'refresh': str(token),
            'access': str(token.access_token),
        }

class UserSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)
        return data
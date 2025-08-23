from rest_framework import serializers
from .models import (
    Profession, Category, 
    Subject, Comment, Training
)


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user'] 

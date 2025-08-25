from rest_framework.generics import  ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from project.pagination import TrainingPagination
from .serializers import (
    TrainingSerializer, CommentSerializer,
    ProfessionSerializer,SubjectSerializer,
    CaegorySerializer,
    )
from .models import ( 
    Training, Comment,Profession,Category,Subject
    )

from rest_framework.exceptions import NotFound

class TrainingListView(ListAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    pagination_class = TrainingPagination

class TrainingDetailView(RetrieveAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer

class CommentListForTrainingView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        training_id = self.kwargs.get('pk')
        try:
            training=Training.objects.get(pk=training_id)
        except Training.DoesNotExist:
            raise NotFound({"error": "Training not found"})
        return Comment.objects.filter(training=training.id).order_by('-id')

    

class CommentCreateForTrainingView(CreateAPIView):
    serializer_class = CommentSerializer  
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        training_id = self.kwargs.get('pk')
        try:
            training=Training.objects.get(pk=training_id)
        except Training.DoesNotExist:
            raise NotFound({"error": "Training not found"})
        serializer.save(
            user=self.request.user,
            training= training,
            )

class SubjectListView(ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class CategaryListView(ListAPIView):
    queryset= Category.objects.all()
    serializer_class = CaegorySerializer


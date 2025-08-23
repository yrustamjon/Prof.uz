from django.urls import path
from .views import (
    TrainingListView, TrainingDetailView,CommentListForTrainingView,
    CommentCreateForTrainingView,
    )

urlpatterns = [
    path('trainings/', TrainingListView.as_view(), name='training-list'),
    path('trainings/<int:pk>/', TrainingDetailView.as_view(), name='training-detail'),
    path('trainings/<int:pk>/comments/', CommentListForTrainingView.as_view(), name='comment-list'),
    path('trainings/<int:pk>/comments/create/', CommentCreateForTrainingView.as_view(), name='comment-detail'),
]

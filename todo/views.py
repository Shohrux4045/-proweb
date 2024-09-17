from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task, Comment
from .serializers import TaskSerializer, CommentSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['status', 'due_date']
    ordering_fields = ['due_date', 'created_at']

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(task__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

from rest_framework import serializers
from .models import Task, Comment
from datetime import date


class TaskSerializer(serializers.ModelSerializer):
    def validate_due_date(self, value):
        if value and value < date.today():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'due_date', 'created_at', 'updated_at', 'user']




class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'task', 'user', 'text', 'created_at']
        read_only_fields = ['user', 'created_at']  # Пользователь и время создания назначаются автоматически

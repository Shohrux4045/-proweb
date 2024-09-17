from django.contrib import admin
from .models import Task, Comment

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'due_date', 'created_at', 'updated_at', 'user')
    list_filter = ('status', 'due_date', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'text', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('text',)
    ordering = ('-created_at',)

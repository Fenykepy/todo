from rest_framework import serializers

from task.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('url', 'description', 'completed', 'due_time', 'date_edited')
        read_only_fields = ('date_edited')

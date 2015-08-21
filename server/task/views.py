from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from task.serializers import *
from task.models import Task

from todo.permissions import IsOwner

class TaskList(generics.ListCreateAPIView):
    """
    API endpoint that presents a list of tasks and allows new
    tasks to be created.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that presents a specific task and allows to
    update or delete it.
    """
    serializer_class = TaskSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


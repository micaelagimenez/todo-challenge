from rest_framework import generics, filters
from todo import models
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ListTask(generics.ListCreateAPIView):
    """
    API view to retrieve list of tasks or create new
    """
    queryset = models.Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['date']
    search_fields = ['description']

class DetailTask(generics.RetrieveDestroyAPIView):
    """
    API view to retrieve or delete a task
    """
    queryset = models.Task.objects.all()
    serializer_class = TaskSerializer
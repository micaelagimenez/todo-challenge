from rest_framework import generics, filters
from todo import models
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend

#lists, creates and filters tasks
class ListTask(generics.ListCreateAPIView):
    queryset = models.Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['date']
    search_fields = ['description']

#allows to see detail of a task
class DetailTask(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Task.objects.all()
    serializer_class = TaskSerializer
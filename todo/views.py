from rest_framework import generics, filters
from todo import models
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend

import logging

logger = logging.getLogger('todo')

class ListTask(generics.ListCreateAPIView):
    """
    API view to retrieve list of tasks or create new tasks
    """
    queryset = models.Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['date']
    search_fields = ['description']

    def get(self, request, *args, **kwargs):
        logger.info('List of tasks retrieved')
        return super().get(request,*args,*kwargs)

class DetailTask(generics.RetrieveDestroyAPIView):
    """
    API view to retrieve or delete a task
    """
    queryset = models.Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        logger.info('Individual task retrieved')
        return super().get(request,*args,*kwargs)
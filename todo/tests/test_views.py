from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from todo.models import Task

class CreateTaskTest(APITestCase):
    def setUp(self):
        self.data = {'title': 'title', 'description': 'desc', 'completed': False}

    def test_can_create_task(self):
        response = self.client.post(reverse('task-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ListTaskTest(APITestCase):
    def setUp(self):
        self.data = {'title': 'title', 'description': 'desc', 'completed': False}
   
    def test_can_list_task(self):
        response = response = self.client.get(reverse('task-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class DeleteTaskTest(APITestCase):
    def setUp(self):
        self.data = Task.objects.create(title= 'title', description= 'desc', completed= False)

    def test_can_delete_task(self):
        response = self.client.delete(reverse('task-detail', args=(self.data.pk,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class RetrieveTaskDetailsTest(APITestCase):
    def setUp(self):
        self.data = Task.objects.create(title= 'title', description= 'desc', completed= False)

    def test_can_retrieve_task_details(self):
        response = self.client.get(reverse('task-detail', args=(self.data.pk,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
from django.test import TestCase
from todo.models import Task

class TaskTest(TestCase):

    def setUp(self):
        Task.objects.create(title='Read book', description='Until page 100', completed=False, date='2021-08-01')

    def test_title(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_description(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_completed_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('completed').verbose_name
        self.assertEqual(field_label, 'completed')

    def test_date(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

    def test_title_max_length(self):
        task = Task.objects.get(id=1)
        max_length = task._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)
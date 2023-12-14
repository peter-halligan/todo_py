from django.test import TestCase
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from ..models import TodoItem

class TodoItemModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='testuser', password='12345')
        TodoItem.objects.create(owner_id=user.pk, title='first todoitem', description='a description here', is_done=False, date_completed=None, date_created=timezone.now())

    def test_title_label(self):
        todoitem = TodoItem.objects.get(id=1)
        field_label = todoitem._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_description_label(self):
        todoitem = TodoItem.objects.get(id=1)
        field_label = todoitem._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')
    
    def test_is_done_label(self):
        todoitem = TodoItem.objects.get(id=1)
        field_label = todoitem._meta.get_field('is_done').verbose_name
        self.assertEquals(field_label, 'is done')
    
    def test_date_completed_label(self):
        todoitem = TodoItem.objects.get(id=1)
        field_label = todoitem._meta.get_field('date_completed').verbose_name
        self.assertEquals(field_label, 'date completed')

    def test_date_created_label(self):
        todoitem = TodoItem.objects.get(id=1)
        field_label = todoitem._meta.get_field('date_created').verbose_name
        self.assertEquals(field_label, 'date created')

    def test_title_max_length(self):
        todoitem = TodoItem.objects.get(id=1)
        max_length = todoitem._meta.get_field('title').max_length
        self.assertEquals(max_length, 256)

    def test_description_max_length(self):
        todoitem = TodoItem.objects.get(id=1)
        max_length = todoitem._meta.get_field('description').max_length
        self.assertEquals(max_length, None)
    
    def test_is_done_default(self):
        todoitem = TodoItem.objects.get(id=1)
        default = todoitem._meta.get_field('is_done').default
        self.assertEquals(default, False)
    
    def test_date_completed_null(self):
        todoitem = TodoItem.objects.get(id=1)
        null = todoitem._meta.get_field('date_completed').null
        self.assertEquals(null, True)

    def test_title_content(self):
        todoitem = TodoItem.objects.get(id=1)
        expected_object_name = f'{todoitem.title}'
        self.assertEquals(expected_object_name, 'first todoitem')

    def test_description_content(self):
        todoitem = TodoItem.objects.get(id=1)
        expected_object_name = f'{todoitem.description}'
        self.assertEquals(expected_object_name, 'a description here')
# Create your tests here.

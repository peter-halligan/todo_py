from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from ..models import ProjectItem, TodoItem


class TodoItemModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="testuser", password="12345")
        TodoItem.objects.create(
            owner_id=user.pk,
            title="first todoitem",
            description="a description here",
            is_done=False,
            date_completed=None,
            date_created=timezone.now(),
        )
        ProjectItem.objects.create(
            owner_id=user.pk,
            title="first projectitem",
            description="a description here",
            is_done=False,
            date_completed=None,
            date_created=timezone.now(),
        )

    def test_todo_title_label(self):
        todoitem = TodoItem.objects.get(id=1)
        field_label = todoitem._meta.get_field("title").verbose_name
        self.assertEquals(field_label, "title")

    def test_todo_description_label(self):
        todoitem = TodoItem.objects.get(id=1)
        field_label = todoitem._meta.get_field("description").verbose_name
        self.assertEquals(field_label, "description")

    def test_todo_is_done_label(self):
        todoitem = TodoItem.objects.get(id=1)
        field_label = todoitem._meta.get_field("is_done").verbose_name
        self.assertEquals(field_label, "is done")

    def test_todo_date_completed_label(self):
        todoitem = TodoItem.objects.get(id=1)
        field_label = todoitem._meta.get_field("date_completed").verbose_name
        self.assertEquals(field_label, "date completed")

    def test_todo_date_created_label(self):
        todoitem = TodoItem.objects.get(id=1)
        field_label = todoitem._meta.get_field("date_created").verbose_name
        self.assertEquals(field_label, "date created")

    def test_todo_title_max_length(self):
        todoitem = TodoItem.objects.get(id=1)
        max_length = todoitem._meta.get_field("title").max_length
        self.assertEquals(max_length, 256)

    def test_todo_description_max_length(self):
        todoitem = TodoItem.objects.get(id=1)
        max_length = todoitem._meta.get_field("description").max_length
        self.assertEquals(max_length, None)

    def test_todo_is_done_default(self):
        todoitem = TodoItem.objects.get(id=1)
        default = todoitem._meta.get_field("is_done").default
        self.assertEquals(default, False)

    def test_todo_date_completed_null(self):
        todoitem = TodoItem.objects.get(id=1)
        null = todoitem._meta.get_field("date_completed").null
        self.assertEquals(null, True)

    def test_todo_title_content(self):
        todoitem = TodoItem.objects.get(id=1)
        expected_object_name = f"{todoitem.title}"
        self.assertEquals(expected_object_name, "first todoitem")

    def test_todo_description_content(self):
        todoitem = TodoItem.objects.get(id=1)
        expected_object_name = f"{todoitem.description}"
        self.assertEquals(expected_object_name, "a description here")

    def test_project_title_label(self):
        project = ProjectItem.objects.get(id=1)
        field_label = project._meta.get_field("title").verbose_name
        self.assertEquals(field_label, "title")

    def test_project_description_label(self):
        project = ProjectItem.objects.get(id=1)
        field_label = project._meta.get_field("description").verbose_name
        self.assertEquals(field_label, "description")

    def test_project_is_done_label(self):
        project = ProjectItem.objects.get(id=1)
        field_label = project._meta.get_field("is_done").verbose_name
        self.assertEquals(field_label, "is done")

    def test_project_date_completed_label(self):
        project = ProjectItem.objects.get(id=1)
        field_label = project._meta.get_field("date_completed").verbose_name
        self.assertEquals(field_label, "date completed")

    def test_project_date_created_label(self):
        project = ProjectItem.objects.get(id=1)
        field_label = project._meta.get_field("date_created").verbose_name
        self.assertEquals(field_label, "date created")


# Create your tests here.

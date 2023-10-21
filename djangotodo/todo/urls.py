from django.urls import path

from . import views

urlpatterns = [ path("", views.todos, name="todos"),
               path("add", views.todo_form, name="todo_form"),
               path("<int:pk>/", views.todo_form, name="todo_update"),
                path("<int:pk>/", views.todo, name="todo"),
                 path("<int:pk>/delete/", views.delete, name="delete"), ]
from django.urls import path
from .views import home,deleteTodo,noteCompleted
urlpatterns = [
    path("",home),
    path("deleteTodo/<int:id>/",deleteTodo,name='deleteTodo'),
    path("noteCompleted/<int:id>/",noteCompleted,name='noteCompleted'),


]
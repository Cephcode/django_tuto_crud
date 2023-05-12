
from django.urls import path
from .views import home, delete_data, modify_data
urlpatterns = [
    path("", home,name="addandshow"),
    path("delete/<int:id>", delete_data, name="delete_data"),
    path("modify/<int:id>", modify_data, name="modify_data"),


]

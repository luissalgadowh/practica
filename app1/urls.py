from django.urls import path

from .views import index, add_person

urlpatterns = [
    path('', index, name="index"),
    path('add-person/', add_person, name="add_person"),
]
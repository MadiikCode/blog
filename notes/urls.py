from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_note, name='add_note'),  # Это важно!
    path('', views.note_list, name='note_list'),
]


from django.urls import path

from . import views

urlpatterns = [
    path('', views.read, name='read'),
    path('create/', views.create, name='create'),
    path('update/<int:note_id>', views.update, name='update'),
    path('delete/<int:note_id>', views.delete, name='delete'),
]
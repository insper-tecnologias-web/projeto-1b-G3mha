from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:note_id>', views.update, name='update'),
    path('api/notes/<int:note_id>/', views.api_note),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_room_list, name='chat_room_list'),
    path('create/', views.create_chat_room, name='create_chat_room'),
    path('delete/<int:room_id>/', views.delete_chat_room, name='delete_chat_room'),
    path('chat/<int:room_id>/', views.chat, name='chat'),
    path('chat/<int:room_id>/history/', views.get_chat_history, name='get_chat_history'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_list),
    path('chat/<int:chat_id>/', views.chat),
    path('chat/<int:chat_id>/add_conversation/', views.add_conversation),
]


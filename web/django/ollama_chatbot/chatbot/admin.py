from django.contrib import admin
from .models import Chat, Conversation

# Register your models here.


class ChatAdmin(admin.ModelAdmin):
    search_fields = ["description"]
    list_display = ["description", "updated_at"]


class ConversationAdmin(admin.ModelAdmin):
    search_fields = ["question"]
    list_display = ["chat_room", "question", "created_at"]


admin.site.register(Chat, ChatAdmin)
admin.site.register(Conversation, ConversationAdmin)

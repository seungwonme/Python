from django.db import models

class Chat(models.Model):
    description = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

class Conversation(models.Model):
    chat_room = models.ForeignKey(Chat, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.question) <= 50:
            return self.question
        return f"{self.question[:47]}..."

from django.shortcuts import render, get_object_or_404
from django.http import StreamingHttpResponse, JsonResponse
from .models import Chat, Conversation
from .ollama import get_ollama_response

# Create your views here.

def chat_list(request):
    chat_list = Chat.objects.all()
    context = {
        'chat_list': chat_list
    }
    return render(request, 'chatbot/chat_list.html', context)

def chat(request, chat_id):
    chat_room = get_object_or_404(Chat, id=chat_id)
    if request.method == 'POST':
        question = request.POST['question']
        return StreamingHttpResponse(get_ollama_response(question, chat_room))
    elif request.method == 'GET':
        conversations = Conversation.objects.filter(chat_room=chat_room).order_by('-id')[:10]
        context = {
            'chat_room': chat_room,
            'conversations': conversations
        }
    return render(request, 'chatbot/chat.html', context)

def add_conversation(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    question = request.POST['question']
    answer = request.POST['answer']
    conversation = Conversation(chat_room=chat, question=question, answer=answer)
    conversation.save()
    return chat(request, chat_id)

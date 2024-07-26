from django.shortcuts import render, redirect, get_object_or_404
from django.http import StreamingHttpResponse, JsonResponse
from .models import ChatRoom, Conversation
import requests
import json

def chat_room_list(request):
    chat_rooms = ChatRoom.objects.order_by('-created_at')
    return render(request, 'chatbot/chat_room_list.html', {'chat_rooms': chat_rooms})

def create_chat_room(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        ChatRoom.objects.create(name=name)
    return redirect('chat_room_list')

def delete_chat_room(request, room_id):
    chat_room = get_object_or_404(ChatRoom, id=room_id)
    chat_room.delete()
    return redirect('chat_room_list')

def chat(request, room_id):
    chat_room = get_object_or_404(ChatRoom, id=room_id)
    if request.method == 'POST':
        question = request.POST.get('question')
        return StreamingHttpResponse(get_ollama_response(question, chat_room))
    elif request.method == 'GET':
        conversations = chat_room.conversations.order_by('-id')[:10]
        context = {
            'chat_room': chat_room,
            'conversations': [
                {'question': conv.question, 'answer': conv.answer}
                for conv in reversed(conversations)
            ]
        }
        return render(request, 'chatbot/chat.html', context)

def get_chat_history(request, room_id):
    chat_room = get_object_or_404(ChatRoom, id=room_id)
    conversations = chat_room.conversations.order_by('-id')[:10]
    history = [
        {'question': conv.question, 'answer': conv.answer}
        for conv in reversed(conversations)
    ]
    return JsonResponse({'history': history})

def get_ollama_response(prompt, chat_room):
    url = "http://localhost:11434/api/generate"
    
    # 최근 대화 내용을 가져옵니다
    conversations = Conversation.objects.order_by('-id')[:5]  # 최근 5개만 가져옵니다
    context = "\n".join([f"Human: {conv.question}\nAI: {conv.answer}" for conv in reversed(conversations)])
    
    data = {
        "model": "llama3.1",
        "prompt": f"너는 AI야. 한국어에 대한 질문은 반드시 한국어로 답변해.\n{context}\nHuman: {prompt}\nAI:",
        "stream": True
    }
    
    response = requests.post(url, json=data, stream=True)
    full_response = ""
    
    for line in response.iter_lines():
        if line:
            json_data = json.loads(line.decode('utf-8'))
            if 'response' in json_data:
                chunk = json_data['response']
                full_response += chunk
                yield chunk
            if json_data.get('done', False):
                break
    
    Conversation.objects.create(chat_room=chat_room, question=prompt, answer=full_response)

from django.contrib import admin
from .models import Chat, Conversation

from django.contrib import admin
from .models import Chat, Conversation

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('chat', 'query', 'response', 'created_at')  


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChatViewSet, ConversationViewSet

router = DefaultRouter()
router.register(r'chats', ChatViewSet)
router.register(r'conversations', ConversationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

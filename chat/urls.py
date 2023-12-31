from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('send-message/', views.send_message, name='send-message'),
    path('<str:RoomId>', views.room, name='room'),
    path('get/<str:RoomId>/', views.get_messages, name='get-messages')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

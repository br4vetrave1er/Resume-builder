from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('upload_file/', views.upload_file, name='file_upload'),
    path('chat/', views.chat_room, name="chat-room"),
    path('response/', views.chat_response, name="response"),
    path('bot-build/', views.bot_build, name="bot-build"),
    path('get_pdf/', views.view_pdf, name="get-pdf")
]
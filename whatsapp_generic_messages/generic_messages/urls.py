from django.urls import path
from . import views

urlpatterns = [
    path("messagesByCategory/<category_id>", views.get_messages_by_category),
    path("send-message/", views.send_message),
    path("send-message-demo/", views.send_message_demo)
]
from django.urls import path
from . import views

urlpatterns = [
    path("get-history/", views.get_history),
    path("get-history-asc/", views.get_history_asc),
    path("get-history-desc/", views.get_history_desc)
]
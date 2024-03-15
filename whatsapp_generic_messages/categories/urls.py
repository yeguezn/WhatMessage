from django.urls import path
from .views import CategoryView

urlpatterns = [
   path("all-categories/", CategoryView.as_view())
]
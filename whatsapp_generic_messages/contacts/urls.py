from django.urls import path
from . import views

urlpatterns = [
    path("new-contact/", views.create_contact),
    path("update-contact/<int:contact_id>", views.update_contact),
    path("delete-contact/<int:contact_id>", views.delete_contact),
    path("get-contacts/", views.get_contacts),
    path("get-contact/<int:contact_id>", views.get_contact_by_id)
]
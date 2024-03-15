from django.db import models
from django.contrib.auth.models import User
from generic_messages.models import GenericMessage
from contacts.models import Contact

# Create your models here.

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    message = models.ForeignKey(GenericMessage, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=True)

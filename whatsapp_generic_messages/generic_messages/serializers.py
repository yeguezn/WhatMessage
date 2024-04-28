from rest_framework import serializers
from .models import GenericMessage
from contacts.models import Contact
import re
from generic_messages.models import GenericMessage

class GenericMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenericMessage
        fields = ["id", "content"]

class SendMessageSerializer(serializers.Serializer):
    message = serializers.CharField()
    phone_number = serializers.CharField(max_length=20)

    def validate_phone_number(self, value):

        if not re.search("^\\+(?:[0-9] ?){6,14}[0-9]$", value):
            raise serializers.ValidationError(
                "The phone number must match with the international format."
            )

        return value
    
    def validate_message(self, value):
        if not GenericMessage.objects.filter(content=value):
            raise serializers.ValidationError("This message doesn\'t exist.")
        
        return value        
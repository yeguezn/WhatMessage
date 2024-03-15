from rest_framework import serializers
from .models import Contact
import re

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ("id", "full_name", "phone_number")
    
    def validate_phone_number(self, value):
        if not re.search("^\+(?:[0-9] ?){6,14}[0-9]$", value):
            raise serializers.ValidationError(
                "The phone number must match with the international format."
            )
        
        return value
    
    
    


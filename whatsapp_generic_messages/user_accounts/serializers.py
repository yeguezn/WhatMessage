from rest_framework import serializers
from django.contrib.auth.models import User

class UserAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
    
    def validate_email(self, value):
        if User.objects.filter(email=value):
            raise serializers.ValidationError("This email already exists.")
        
        return value
    
   
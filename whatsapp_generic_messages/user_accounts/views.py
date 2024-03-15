from .serializers import UserAccountSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["POST"])
def signup(request):
    serializer = UserAccountSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data["username"])
        user.set_password(request.data["password"])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"user":serializer.data, "token":token.key})
        
    return Response(serializer.errors, status=400)


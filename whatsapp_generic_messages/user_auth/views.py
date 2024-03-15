from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from user_accounts.serializers import UserAccountSerializer
from rest_framework import authentication, permissions
from rest_framework.decorators import authentication_classes, permission_classes, api_view

# Create your views here.
@api_view(["POST"])
def signin(request):
    try:
        user = User.objects.get(email=request.data["email"])

        if not user.check_password(request.data["password"]):
            return Response({"password":"Your password is incorrect."}, status=400)
    
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserAccountSerializer(instance=user)
        return Response({"token":token.key, "user":serializer.data})
    except User.DoesNotExist:
        return Response({"email":"This user doesn't exist."}, status=400)

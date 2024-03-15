from .models import GenericMessage
from categories.models import Category
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import GenericMessagesSerializer, SendMessageSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from urllib.parse import quote
from contacts.models import Contact
from history.models import History

# Create your views here.

@api_view(["GET"])
def get_messages_by_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    all_messages_by_category = [message for message in GenericMessage.objects.filter(category=category)]
    serialized = GenericMessagesSerializer(all_messages_by_category, many=True)
    return Response(serialized.data)


@api_view(["POST"])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def send_message(request):
    serializer = SendMessageSerializer(data=request.data)

    if serializer.is_valid():

        if not Contact.objects.filter(phone_number=request.data['phone_number'], 
        user=request.user):
            
            return Response({"detail":"This contact doesn\'t exist."}, status=400)
        
        message = GenericMessage.objects.get(content=request.data['message'])
        contact = Contact.objects.get(phone_number=request.data["phone_number"])
        encoded_message = quote(message.content)
        phone_number = request.data['phone_number'][1:]

        url = f"http://wa.me/{phone_number}?text={encoded_message}"

        new_history_record = History(
            user=request.user, 
            contact=contact,
            message=message
        )

        new_history_record.save()

        return Response({"whatsapp_url":url}, status=200)
    
    return Response(serializer.errors, status=400)


@api_view(["POST"])
def send_message_demo(request):
    serializer = SendMessageSerializer(data=request.data)

    if serializer.is_valid():
        encoded_message = quote(request.data['message'])
        phone_number = request.data['phone_number'][1:]

        url = f"http://wa.me/{phone_number}?text={encoded_message}"

        return Response({"whatsapp_url":url}, status=200)
    
    return Response(serializer.errors, status=400)
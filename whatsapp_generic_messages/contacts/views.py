from .models import Contact
from .serializers import ContactSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import authentication_classes, permission_classes, api_view

# Create your views here.
@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_contacts(request, format=None):
    all_contacts = [contact for contact in Contact.objects.all().filter(user=request.user)]
    serializer = ContactSerializer(all_contacts, many=True)
    return Response(serializer.data, status=200)

@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_contact_by_id(request, contact_id=None, format=None):
    
    if contact_id is None:
        return Response({"detail":"Contact id wasn\'t specified."}, status=400)

    if not Contact.objects.filter(id=contact_id, user=request.user):
        return Response({"detail":"This contact doesn\'t exist."}, status=400)

    contact = Contact.objects.get(id=contact_id, user=request.user)
    serializer = ContactSerializer(contact)
    return Response(serializer.data, status=200)

@api_view(["POST"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])  
def create_contact(request, format=None):
    serializer = ContactSerializer(data=request.data)

    if serializer.is_valid():
        new_contact = Contact(
            full_name=request.data["full_name"], 
            phone_number=request.data["phone_number"],
            user = request.user
        )

        new_contact.save()

        return Response(serializer.data, status=200)
        
    return Response(serializer.errors, status=400)

@api_view(["DELETE"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_contact(request, contact_id, format=None):

    if not contact_id:
        return Response(
            {"detail":"The contact_id parameter is not defined."},
            status=400
        )
    
    if not Contact.objects.filter(id=contact_id, user=request.user):
        return Response({"detail":"This contact doesn\'t exist."}, status=400)
    
    Contact.objects.get(id=contact_id, user=request.user).delete()

    return Response({"detail":"The contact has been deleted."}, status=200)

@api_view(["PUT"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_contact(request, contact_id=None, format=None):

    if not contact_id:
        return Response(
            {"detail":"The contact_id parameter is not defined."},
            status=400
        )
    
    if not Contact.objects.filter(id=contact_id, user=request.user):
        return Response({"detail":"This contact doesn\'t exist."}, status=400)
    
    serializer = ContactSerializer(data=request.data)

    if serializer.is_valid():
        contact = Contact.objects.get(id=contact_id)
        contact.full_name = request.data["full_name"]
        contact.phone_number = request.data["phone_number"]
        contact.save()
        return Response(serializer.data, status=200)
    
    return Response(serializer.errors, status=400)
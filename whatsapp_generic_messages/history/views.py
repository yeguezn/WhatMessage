from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from .models import History
from .serializers import HistorySerializer
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

# Create your views here.
@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_history(request):
    user_history = [record for record in History.objects.filter(user=request.user)
    .values(
        "contact__full_name",
        "message__content",
        "message__category__name",
        "date_time"
    )]

    serializer = HistorySerializer(user_history, many=True)
    
    return Response(serializer.data, status=200)

@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_history_asc(request):
    user_history = [record for record in History.objects.filter(user=request.user)
    .order_by("date_time")
    .values(
        "contact__full_name",
        "message__content",
        "message__category__name",
        "date_time"
    )]

    serializer = HistorySerializer(user_history, many=True)

    return Response(serializer.data, status=200)


@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_history_desc(request):
    user_history = [record for record in History.objects.filter(user=request.user)
    .order_by("-date_time")
    .values(
        "contact__full_name",
        "message__content",
        "message__category__name",
        "date_time"
    )]

    serializer = HistorySerializer(user_history, many=True)

    return Response(serializer.data, status=200)

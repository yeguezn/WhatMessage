from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import CategorySerializer
from rest_framework.response import Response
from .models import Category

# Create your views here.
class CategoryView(APIView):
    def get(self, request, format=None):
        categories = [{"id":category.id, "name":category.name} for category in Category.objects.all()]
        serialized_categories = CategorySerializer(categories, many=True)
        return Response({"categories":categories})



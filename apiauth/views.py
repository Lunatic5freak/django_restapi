from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import  IsAuthenticated
from . models import employees
from .serializers import employeesSerializer

# Create your views here.
@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def welcome(request):
    content={"messege":"welcome"}
    return JsonResponse(content)

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def getlist(request):
    employee1=employees.objects.all()
    serializer=employeesSerializer(employee1,many=True)
    return Response(serializer.data)

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def addemployee(request):
    print(request.data)
    serializar=employeesSerializer(data=request.data)
    if serializar.is_valid():
        serializar.save()
    content={"content":"done"}
    return JsonResponse(content)
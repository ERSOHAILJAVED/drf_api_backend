from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from account.serializers import UserRegistrationSerializer


# Create your views here.
class UserResigisterView(APIView):
    def get(self,request):
        return Response({"msg":"hello world"})
    
    def post(self,request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"msg":"Registration successfully"})
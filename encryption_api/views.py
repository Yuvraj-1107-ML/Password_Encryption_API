from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cryptography.fernet import Fernet
from django.conf import settings
from .serializers import EncryptPasswordSerializer



def encryptFunction(param):
 
    user_secret_key = settings.FERNET_SECRET_KEY
    encryptor = Fernet(user_secret_key)
    encrypted_password = encryptor.encrypt(param.encode("utf-8"))
    return encrypted_password
class EncryptPasswordView(APIView):
    def post(self, request):
        serializer = EncryptPasswordSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            encrypted_password = encryptFunction(password)
            return Response({'username': username,'encrypted_password': encrypted_password}, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

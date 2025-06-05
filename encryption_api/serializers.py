from rest_framework import serializers

class EncryptPasswordSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

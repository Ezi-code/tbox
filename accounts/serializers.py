from rest_framework import serializers 
from accounts.models import AccountHolder
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token



class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = AccountHolder
        fields = ('id','username', 'email', 'password', 'gender')

    def create(self, validated_data):
        return super().create(validated_data)
    
    def login(self, validated_data):
        user = authenticate(username=validated_data['username'], password=validated_data['password'])
        token, _ = Token.objects.get_or_create(user=user)
        return super().login(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


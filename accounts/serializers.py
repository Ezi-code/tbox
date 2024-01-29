from rest_framework import serializers 
from accounts.models import AccountHolder

class AccountHolderSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = AccountHolder
        fields = ('id','username', 'email', 'password', 'gender')

    def create(self, validated_data):
        return super().create(validated_data)

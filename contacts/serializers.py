from rest_framework import serializers

from .models import Contract

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('id', 'name', 'email', 'message')

    def create(self, validated_data):
        return Contract.objects.create(**validated_data)    
    
    def update(self, Contract, validated_data: dict):
        Contract.name = validated_data.get('name', Contract.name)
        Contract.email = validated_data.get('email', Contract.email)
        Contract.message = validated_data.get('message', Contract.message)
        Contract.save()
        return Contract


# class SubcontractorSerializer(serializers.ModelSerializer):
#     class Meta:   
#         model = Subcontractor
#         fields = ('id', 'name', 'email', 'message', 'contract')
        
    
from rest_framework import serializers

from .models import Contract, Subcontractor


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ("id", "name", "email", "message", "project", "sub_contractor")

    def create(self, validated_data):
        return Contract.objects.create(**validated_data)

    def update(self, Contract, validated_data: dict):
        Contract.name = validated_data.get("name", Contract.name)
        Contract.email = validated_data.get("email", Contract.email)
        Contract.message = validated_data.get("message", Contract.message)
        Contract.project = validated_data.get("project", Contract.project)
        Contract.sub_contractor = validated_data.get(
            "sub_contractor", Contract.sub_contractor
        )
        Contract.save()
        return Contract


class SubcontractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcontractor
        fields = ("id",)

    def create(self, validated_data):
        return super().create(validated_data)

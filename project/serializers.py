from rest_framework import serializers
from .models import Project
from contacts.models import Subcontractor
from contacts.serializers import SubcontractorSerializer


class ProjectSerializer(serializers.ModelSerializer):
    sub_contractor = SubcontractorSerializer(many=True)

    class Meta:
        model = Project
        fields = ("id", "title", "description", "sub_contractor")

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    def update(self, Project, validated_data: dict):
        Project.title = validated_data.get("title", Project.title)
        Project.description = validated_data.get("description", Project.description)
        Project.sub_contractor.set(validated_data["sub_contractor"])
        Project.save()
        return Project


class ProjectSubcontractorSerializer(serializers.ModelSerializer):
    class Operations:
        ADD = "add"
        REMOVE = "remove"

        choices = (ADD, REMOVE)

    subcontractor_id = serializers.ListField(
        child=serializers.IntegerField(), read_only=True
    )

    subcontractor = SubcontractorSerializer(many=True, read_only=True)

    operations = serializers.ChoiceField(choices=Operations.choices)

    def update(self, instance: Project, validated_data: dict):
        from contacts.models import Subcontractor

        subcontractor_ids = validated_data["subcontractor_id", []]
        for subcontractor_id in subcontractor_ids:
            operations = validated_data["operations"]

            if operations == self.Operations.ADD:
                instance.sub_contractor.add(subcontractor_id)
            elif operations == self.Operations.REMOVE:
                instance.sub_contractor.remove(subcontractor_id)
            instance.save()
            return instance

    class Meta:
        model = Project
        fields = ("subcontractor_id", "subcontractor", "choice")

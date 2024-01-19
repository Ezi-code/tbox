from rest_framework import serializers
from .models import Project
from contacts.models import Subcontractor


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'sub_contractor')
    
    def create(self, validated_data):
        return Project.objects.create(**validated_data)    
    
    def update(self, Project, validated_data: dict):
        Project.title = validated_data.get('title', Project.title)
        Project.description = validated_data.get('description', Project.description)
        Project.sub_contractor.set(validated_data['sub_contractor'])
        Project.save()
        return Project
    


class SubcontractorSerializer(serializers.ModelSerializer):
    class Meta:   
        model = Subcontractor
        fields = ('id',)

    def update(self, Project, validated_data: dict):
        Project.sub_contractor = validated_data.get('id', Project.sub_contractor)
        Project.save()
        return Project
    
    def create(self, validated_data):
        return Subcontractor.objects.create(**validated_data)
    
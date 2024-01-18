from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'start_date', 'end_date', 'is_active', 'contract')
    
    def create(self, validated_data):
        return Project.objects.create(**validated_data)    
    
    def update(self, Project, validated_data: dict):
        Project.name = validated_data.get('name', Project.name)
        Project.description = validated_data.get('description', Project.description)
        Project.start_date = validated_data.get('start_date', Project.start_date)
        Project.end_date = validated_data.get('end_date', Project.end_date)
        Project.is_active = validated_data.get('is_active', Project.is_active)
        Project.contract = validated_data.get('contract', Project.contract)
        Project.save()
        return Project
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from api.to_do.serializers.general_serializers import TaskSerializer, GroupTaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.filter(is_active=True)

class GroupTaskViewSet(viewsets.ModelViewSet):
    serializer_class = GroupTaskSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.filter(is_active=True)



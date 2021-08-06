from rest_framework import serializers
from api.to_do.models import GroupTask,Task
from api.user.serializers.serializers import UserListSerializer

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ['is_active','created_at','modified_at','deleted_at']

    def to_representation(self, instance):
        #state = instance.get_state_display()
        return {
            'id': instance.id,
            'title': instance.title,
            'description': instance.description,
            'is_active': instance.is_active,
            'state':instance.state
        }

class GroupTaskSerializer(serializers.ModelSerializer):
    user = UserListSerializer(many=True,read_only=True)
    task = TaskSerializer(many=True)
    class Meta:
        model=GroupTask
        fields=['id','name','task','user','is_active']

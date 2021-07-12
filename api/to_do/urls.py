from django.urls import path
from rest_framework.routers import DefaultRouter

from api.to_do.views.general_views import TaskViewSet, GroupTaskViewSet

router = DefaultRouter()

router.register(r'tasks',TaskViewSet,basename='task')
router.register(r'group_task',GroupTaskViewSet,basename='groupTask')

urlpatterns=router.urls

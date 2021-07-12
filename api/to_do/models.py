from django.db import models
from api.core.models import BaseModel
from api.user.models import User

# Create your models here.
TO_DO ='TD'
IN_PROGRESS = 'IP'
FINLIZED = 'ED'  

class Task(BaseModel): 
    TASK_CHOICES =[
        (TO_DO,'To do'),
        (IN_PROGRESS,'In progress'), 
        (FINLIZED,'Finalized'),
    ]
    title = models.CharField('Title',max_length=130, null=False, blank=False) 
    description = models.CharField('Description', max_length=255, null=False, blank= False) 
    state = models.CharField('state', max_length=2, choices=TASK_CHOICES, default=TO_DO,null=False, blank=False) 
    class  Meta:
        verbose_name = 'Task'
        verbose_name_plural='Tasks'

class GroupTask(BaseModel):
    name = models.CharField('Name',max_length=100,null=False, blank=False, unique=True)
    user = models.ManyToManyField(User, blank=False, related_name='users') 
    task = models.ManyToManyField(Task, blank=False, related_name='tasks')
    class Meta:
        verbose_name='Group task'
        verbose_name_plural='Group tasks'

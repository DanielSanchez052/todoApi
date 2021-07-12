from django.contrib import admin
from api.to_do.models import GroupTask, Task
# Register your models here.
admin.site.register(Task)
admin.site.register(GroupTask)

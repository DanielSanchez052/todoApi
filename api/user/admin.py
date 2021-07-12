from django.contrib import admin
from api.user.models import User
from django.contrib.sessions.models import Session

# Register your models here.
admin.site.register(User)
admin.site.register(Session)

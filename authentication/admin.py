from django.contrib import admin
from django.contrib.auth.models import ContentType, Permission
from .models import User

# Register your models here.

admin.site.register(ContentType)
admin.site.register(Permission)
admin.site.register(User)

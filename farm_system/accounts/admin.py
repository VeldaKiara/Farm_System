from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from accounts.models import CustomUser

admin.site.register(CustomUser, UserAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from  profiles_api import  models

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name', 'password', 'is_superuser', 'is_staff']


admin.site.register(models.UserProfile, UserAdmin)




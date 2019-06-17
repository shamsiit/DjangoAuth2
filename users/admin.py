from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import ModelAdmin

from .models import AppUser, UserProfile

class AppUserAdmin(UserAdmin):
    model = AppUser
    list_display = ['uuid','email', 'username',]

class UserProfileAdmin(ModelAdmin):
    model = UserProfile
    list_display = ['uuid']    

admin.site.register(AppUser, AppUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

from django.contrib import admin
from accounts.models import User, UserProfile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    pass

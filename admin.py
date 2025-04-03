from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Unregister the default User model first
admin.site.unregister(User)

# Register it again with custom settings
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass  # You can add custom admin settings here

from django.contrib import admin
from .models import UserTable


# Register your models here.
class username(admin.ModelAdmin):
    """User Model admin."""
    list_display = ['id', 'firstName', 'user_id']




admin.site.register(UserTable, username)

from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib.auth.models import Group

from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'auth_provider', 'last_name', 'is_superuser', 'is_active',]
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password', 'first_name', 'last_name', 'middle_name', 'addres', 'upload_user', 'auth_provider', 'is_superuser', 'is_active',)
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Transaction
from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Transaction)

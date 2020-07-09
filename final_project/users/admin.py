from django.contrib import admin

from .models import CustomUser, Transaction


admin.site.register(Transaction)

admin.site.register(CustomUser)

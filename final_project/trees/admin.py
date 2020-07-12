from django.contrib import admin

from .models import Tree


class TreeAdmin(admin.ModelAdmin):
    list_display  = ['name', 'sold', 'owner_id']


admin.site.register(Tree, TreeAdmin)

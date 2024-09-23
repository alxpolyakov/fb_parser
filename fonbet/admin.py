from django.contrib import admin
from .models import RemoteSport


@admin.register(RemoteSport)
class RemoteSportAdmin(admin.ModelAdmin):
    list_display = ['name', 'alias', 'remote_id', 'local_sport']

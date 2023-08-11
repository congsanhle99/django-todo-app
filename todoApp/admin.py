from django.contrib import admin
from .models import Task


class taskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_complete', 'update_at')
    search_fields = ('task',)


# Register your models here.
admin.site.register(Task, taskAdmin)

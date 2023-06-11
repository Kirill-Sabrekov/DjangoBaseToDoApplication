from django.contrib import admin

from .models import ToDoTables, ToDoListItem

admin.site.register(ToDoTables)
admin.site.register(ToDoListItem)
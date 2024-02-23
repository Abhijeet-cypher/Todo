from django.contrib import admin
from .models import todo

# Register your models here.
# admin.site.register(todo)

@admin.register(todo)
class Todo(admin.ModelAdmin):
    list_display = ['user', 'todo_name']
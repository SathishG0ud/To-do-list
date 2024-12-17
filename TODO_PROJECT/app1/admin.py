from django.contrib import admin
from . models import TODOLIST,History

# Register your models here.
@admin.register(TODOLIST)
class AdminTodo(admin.ModelAdmin):
    list_display = ['task','description']


@admin.register(History)
class AdminHistory(admin.ModelAdmin):
    list_display = ['task','description']


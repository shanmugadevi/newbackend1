from django.contrib import admin

# Register your models here.
from .models import Todolist


class TodolistAdmin(admin.ModelAdmin):  # add this
    list_display = ('title', 'description')  # add this


admin.site.register(Todolist, TodolistAdmin)  # add this

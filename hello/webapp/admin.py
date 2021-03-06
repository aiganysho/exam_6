from django.contrib import admin
from webapp.models import Guestbook


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'author', 'email', 'text', 'time_of_creation', 'time_of_update']
    list_filter = ['author', 'status', 'text']
    search_fields = ['status', 'describe', 'description']
    fields = ['status', 'author', 'email', 'text', 'time_of_creation', 'time_of_update']
    readonly_fields = ['id', 'time_of_creation', 'time_of_update']


admin.site.register(Guestbook, BookAdmin)
from django.contrib import admin
from . models import *

# Register your models here.

class ListAdmin(admin.ModelAdmin):
    list_display = ('title','subject','status')
    list_filter = ('status', 'created_at', 'updated_at')
    search_fields = (
    	'title',
    	'subject'
    )
    date_hierarchy = 'created_at'
    empty_value_display = '-empty-'
    #actions = None

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        obj.save()

admin.site.register(List, ListAdmin)
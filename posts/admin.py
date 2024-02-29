from django.contrib import admin
from posts.models import *
# Register your models here.
class commentadmin(admin.TabularInline):
    model = comment
    fields = ['Text',]
    extra = 0

@admin.register(post)
class postadmin(admin.ModelAdmin):
    list_display = ['id','title','is_enable','publish_date','created_time']
    inlines = [commentadmin,]

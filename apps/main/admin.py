from django.contrib import admin
from apps.main.models import Main
# Register your models here.

@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'logo', 'is_activ')
    search_fields = ('title', )
    list_filter = ('is_activ' ,)
    list_editable = ('is_activ', )
    ordering = ('-created_at',)

from django.contrib import admin
from .models import Va_hora

class HoraAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Register your models here.
admin.site.register(Va_hora,HoraAdmin)
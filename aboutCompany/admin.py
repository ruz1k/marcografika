from django.contrib import admin
from .models import MainInfo, Technologies, Clients


class MainInfoAdmin(admin.ModelAdmin):
    list_display = ['information']
admin.site.register(MainInfo, MainInfoAdmin)

class TechnologiesAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Technologies, TechnologiesAdmin)

class ClientsAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Clients, ClientsAdmin)
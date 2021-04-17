from django.contrib import admin
from .models import OrderList

class OrderServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(OrderList, OrderServiceAdmin)
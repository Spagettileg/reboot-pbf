from django.contrib import admin
from .models import Order, OrderLineItem


"""
Both Order & OrderLineItem models added to ensure they can be edited
via the admin panel
"""


class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )

admin.site.register(Order, OrderAdmin)

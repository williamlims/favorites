from django.contrib import admin

from .models import Customer, FavoriteList

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_display = ('name', 'email')

@admin.register(FavoriteList)
class FavoriteListAdmin(admin.ModelAdmin):
	list_display = ('customer_id', 'product_id')
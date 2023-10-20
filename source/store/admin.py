# admin.py
from django.contrib import admin
from .models import Category, Product, CartItem, BillingInformation

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'category', 'stock')
    list_filter = ('category',)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('session', 'user', 'product', 'quantity')

@admin.register(BillingInformation)
class BillingInformationAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'address', 'city', 'state', 'postal_code', 'phone_number')

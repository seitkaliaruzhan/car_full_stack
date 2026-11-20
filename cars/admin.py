from django.contrib import admin
from .models import Car, Owner

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'color', 'registration_number', 'year', 'price', 'owner')
    list_filter = ('brand', 'year')
    search_fields = ('brand', 'model', 'registration_number')
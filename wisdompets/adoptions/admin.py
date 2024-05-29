from django.contrib import admin

from .models import Pet
# Register your models here.

@admin.register(Pet) # Decorator
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed', 'age', 'sex']
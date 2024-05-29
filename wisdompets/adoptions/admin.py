from django.contrib import admin

from .models import Pet
# Register your models here.

@admin.register(Pet) # Decorator
class PetAdmin(admin.ModelAdmin):
    pass # Makes this a valid class.
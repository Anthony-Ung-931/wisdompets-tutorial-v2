from django.shortcuts import render
from django.http import Http404

from .models import Pet

def home(request):
    pets = Pet.objects.all()
    return render(request, template_name='home.html', 
                    context={'pets': pets,})

def pet_detail(request, pet_id):
    try:
        pet = Pet.objects.id(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('pet not found')
    return render(request, template_name='pet.detail.html', 
                    context={'pet': pet,})

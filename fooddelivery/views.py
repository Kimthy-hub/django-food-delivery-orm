from django.shortcuts import render

from .models import FoodItem


def home(request):
    foods = FoodItem.objects.all()
    return render(request, 'fooddelivery/index.html', {'foods': foods})


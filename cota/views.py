from django.shortcuts import render
from .models import *


def categories(request):
    return {
        'categories': Category.objects.all()
    }

def home(request):
    offers = Offer.objects.all()

    context = {'offers': 'offers'}
    return render(request, 'cota/main.html', context)

def top_deals(request):
    context = {}
    return render(request, 'cota/top_deals.html', context)
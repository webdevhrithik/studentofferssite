from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'cota/main.html', context)

def top_deals(request):
    context = {}
    return render(request, 'cota/top_deals.html', context)
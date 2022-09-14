from multiprocessing import context
from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    data_katalog = CatalogItem.objects.all()
    context = {
        'list_katalog' : data_katalog,
        'nama'  : 'Bagas Shalahuddin Wahid',
        'npm'   : '2106708904'
    }
    return render(request, "katalog.html", context)

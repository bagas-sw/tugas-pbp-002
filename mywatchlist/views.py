from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

def show_mywatchlist(request):
    data_mywatchlist = MyWatchList.objects.all()
    context = {
        'list_mywatchlist': data_mywatchlist,
        'nama': 'Bagas',
        'npm' : '2106708904'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

def show_json(request):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")

def show_json_by_id(request, id):
    data_mywatchlist = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")

def show_xml_by_id(request, id):
    data_mywatchlist = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

def show_html(request):
    data_mywatchlist = MyWatchList.objects.all()
    context = {
        'list_mywatchlist': data_mywatchlist,
        'nama': 'Bagas',
        'npm' : '2106708904'
    }
    return render(request, "mywatchlist.html", context)

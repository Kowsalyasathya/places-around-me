from django.shortcuts import render

def map(request):
    return render(request, "mapapp/map.html")

def metrostation(request):
    return render(request, "mapapp/metrostation.html")

def sangeetha(request):
    return render(request, "mapapp/sangeetha.html")

def market(request):
    return render(request, "mapapp/market.html")

def busstand(request):
    return render(request, "mapapp/busstand.html")

def kuru(request):
    return render(request, "mapapp/kuru.html")    




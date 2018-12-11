from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.gis.geos import Point
from .models import *
from django.contrib.gis.db.models import Q

def home(request):
    return render(request, 'index.html')


def list(request):
    if request.method == 'POST':
        search = request.POST['search']

        if search:
            match1 = Restaurant.objects.filter(
                Q(restaurant__startswith=search) |
                Q(rating__icontains=search) |
                Q(type__startswith=search) |
                Q(features__icontains=search)
            )
            if match1:
                return render(request, 'listing.html', {"match1": match1})

            hospital = Hospital.objects.filter(
                Q(hospital_n__startswith=search) |
                Q(hospital_r__icontains=search) |
                Q(contact_nu__startswith=search) |
                Q(address__icontains=search)
            )
            if hospital:
                return render(request, 'listing.html', {"hospital": hospital})

            market = Market.objects.filter(
                Q(market_nam__startswith=search) |
                Q(rating__icontains=search) |
                Q(location__startswith=search) |
                Q(longitude__icontains=search)
            )
            if market:
                return render(request, 'listing.html', {"market": market})

            police = PoliceStation.objects.filter(
                Q(police_sta__icontains=search) |
                Q(rating__icontains=search) |
                Q(contact_nu__startswith=search) |
                Q(latitude__icontains=search)
            )
            if police:
                return render(request, 'listing.html', {"police": police})

            match = Fort.objects.filter(
                Q(title__startswith=search) |
                Q(rating__icontains=search) |
                Q(category__startswith=search) |
                Q(descriptio__icontains=search)
            )
            if match:
                return render(request, 'listing.html', {"match": match})
            else:
                return HttpResponse("No result Found")
        else:
            return HttpResponseRedirect('/')

    args = {
        "users": Fort.objects.all(),
    }
    return render(request, 'index.html', args)


def details(request):
    return render(request, 'detail.html')

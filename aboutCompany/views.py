from django.shortcuts import render
from .models import MainInfo, Technologies, Clients


def aboutUs(request, category_slug=None):
    mainInfoAboutUs = MainInfo.objects.filter()
    technologiesAboutUs = Technologies.objects.filter()
    clientsAboutUs = Clients.objects.filter()
    return render(request, 'aboutCompany/aboutCompany.html', {'info': mainInfoAboutUs, 'technologies': technologiesAboutUs, 'clients': clientsAboutUs})

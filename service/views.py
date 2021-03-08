from django.shortcuts import render

def service_list(request):
    return render(request, 'service/service.html', {})

# Create your views here.

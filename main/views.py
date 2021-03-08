from django.shortcuts import render

def renderIndex(request):
    return render(request, 'main/home.html', {})
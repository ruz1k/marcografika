from django.shortcuts import render, get_object_or_404
from .models import PhotoMedia
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def media_photo(request, category_slug=None):
    category = None
    mediaFile = PhotoMedia.objects.filter()
    paginator = Paginator(mediaFile, 16)
    page = request.GET.get('page')
    try:
        mediaFile = paginator.page(page)
    except PageNotAnInteger:
        mediaFile = paginator.page(1)
    except EmptyPage:
        mediaFile = paginator.page(paginator.num_pages)
    return render(request, 'mediabank/mediabank.html', {'mediaFile': mediaFile})

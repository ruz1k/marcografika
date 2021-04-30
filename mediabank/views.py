from django.shortcuts import render
from .models import PhotoMedia, VideoMedia
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def media_photo(request, category_slug=None):
    category = None
    mediaFile = PhotoMedia.objects.filter()
    mediaFileVideo = VideoMedia.objects.filter()
    paginator = Paginator(mediaFile, 16)
    paginatorVideo = Paginator(mediaFileVideo, 4)
    page = request.GET.get('page')
    try:
        mediaFileVideo = paginatorVideo.page(page)
        mediaFile = paginator.page(page)
    except PageNotAnInteger:
        mediaFileVideo = paginatorVideo.page(1)
        mediaFile = paginator.page(1)
    except EmptyPage:
        mediaFileVideo = paginatorVideo.page(paginatorVideo.num_pages)
        mediaFile = paginator.page(paginator.num_pages)
    return render(request, 'mediabank/mediabank.html', {'mediaFile': mediaFile, 'mediaFileVideo': mediaFileVideo})

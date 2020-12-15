from django.shortcuts import render, get_object_or_404
from .models import Gallery


def gallery(request):
    picture = Gallery.objects.all()
    return render(request, 'gallery/gallery.html', {'pictures': picture})

from django.shortcuts import render
from .models import Yazi


# Create your views here.

def yazi_view(request, slug):
    yazimiz = Yazi.objects.get(slug=slug)
    yazimetin = yazimiz.metin
    return render(request, "reader.html", {"yazimiz": yazimiz, "yazimetin": yazimetin})

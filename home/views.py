from django.shortcuts import render
from yazi.models import Yazi
from django.core.paginator import Paginator

# Create your views here.


def home_view(request):
    kelime = request.GET.get("kelime")
    if kelime:
        yazilar = Yazi.objects.filter(baslik__contains=kelime)
        yazilar |= Yazi.objects.filter(yazar__contains=kelime)
    else:
        yazilar = Yazi.objects.all()

    paginator = Paginator(yazilar, 12)
    page_number = request.GET.get('sayfa')
    page_obj = paginator.get_page(page_number)

    mevcutsayfa = "2"
    return render(request, "index.html", {"mevcutsayfa": mevcutsayfa, "page_obj": page_obj})

from django.contrib import admin
from .models import Yazi


# Register your models here.

class AdminYazi(admin.ModelAdmin):
    list_display = ["baslik", "slug"]
    list_display_links = ["slug"]
    list_filter = ["slug"]
    search_fields = ["baslik", "metin"]
    list_editable = ["baslik"]

    class Meta:
        model = Yazi


admin.site.register(Yazi, AdminYazi)

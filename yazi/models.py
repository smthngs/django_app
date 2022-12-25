from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils.crypto import get_random_string


# Create your models here.
class Yazi(models.Model):
    baslik = models.CharField(max_length=120)
    yazar = models.CharField(max_length=150, null=True, blank=True)
    metin = models.TextField()
    image = models.FileField(null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False, max_length=130)
    goruntulenme = models.IntegerField(default=0)

    def __str__(self):
        return self.baslik

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})

    def get_unique_slug(self):
        slug = slugify(self.baslik)
        unique_slug = slug
        while Yazi.objects.filter(slug=unique_slug).exists():
            unique_slug = slug + "-" + get_random_string(length=4)
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_unique_slug()
        return super(Yazi, self).save(*args, **kwargs)


class Yorum(models.Model):
    yazi = models.ForeignKey(Yazi, on_delete=models.CASCADE, related_name="yorumlar")
    metin = models.TextField()
    yayinTarihi = models.DateTimeField(auto_now_add=True)

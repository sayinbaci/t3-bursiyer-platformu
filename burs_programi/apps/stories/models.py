from django.db import models
from django.utils.translation import gettext_lazy as _
from urllib.parse import urlparse, parse_qs
from django.utils.text import slugify

class Story(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='stories/')
    slug = models.SlugField(unique=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Interview(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.URLField()

    def __str__(self):
        return self.title

    def embed_url(self):

        url_data = urlparse(self.video_url)
        query = parse_qs(url_data.query)
        video_id = query.get("v")
        if video_id:
            return f"https://www.youtube.com/embed/{video_id[0]}"
        return self.video_url


class Testimonial(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Ad"))
    surname = models.CharField(max_length=100, verbose_name=_("Soyad"))
    content = models.TextField(verbose_name=_("Yorum"))
    is_featured = models.BooleanField(default=False)
    tag = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='testimonials/', null=True, blank=True, verbose_name=_("Profil Fotoğrafı"))

    def __str__(self):
        return self.name + ' ' + self.surname

from django.db import models
from django.utils.text import slugify

class NewsCategory(models.Model):
    """
    Haber kategorilerini temsil eder. (Örn: Duyuru, Etkinlik, Basın)
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class NewsArticle(models.Model):
    """
    Tek bir haber kaydını temsil eder. Başlık, içerik, görsel ve tarih içerir.
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='news/')
    category = models.ForeignKey(NewsCategory, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

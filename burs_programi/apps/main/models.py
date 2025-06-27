from django.db import models
from django.utils.text import slugify
from django.utils.translation import get_language, gettext_lazy as _
from modeltranslation.utils import get_translation_fields
from ckeditor.fields import RichTextField
from django.urls import reverse


class ScholarshipProgram(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Başlık"))
    slug = models.SlugField(unique=True, verbose_name=_("Slug"))
    description = RichTextField(verbose_name=_("Açıklama"))
    image = models.ImageField(upload_to='scholarship_programs/', verbose_name=_("Görsel"))
    tag = models.CharField(max_length=100, verbose_name=_("Etiket"))

    def get_absolute_url(self):
        return reverse('scholarship_program_detail', args=[self.slug])

    class Meta:
        verbose_name = _("Burs Programı")
        verbose_name_plural = _("Burs Programları")

    def save(self, *args, **kwargs):
        if not self.slug:
            lang = get_language()
            title = getattr(self, f"title_{lang}", None) or self.title
            self.slug = slugify(title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class FAQ(models.Model):
    scholarship_program = models.ForeignKey(
        ScholarshipProgram,
        on_delete=models.CASCADE,
        related_name='faqs',
        verbose_name=_("Burs Programı")
    )
    question = models.CharField(max_length=255, verbose_name=_("Soru"))
    answer = models.TextField(verbose_name=_("Cevap"))

    class Meta:
        verbose_name = _("SSS")
        verbose_name_plural = _("Sıkça Sorulan Sorular")

    def __str__(self):
        return self.question

class Application(models.Model):
    full_name = models.CharField(max_length=200, verbose_name=_("Ad Soyad"))
    identity_number = models.CharField(max_length=11, unique=True, verbose_name=_("T.C. Kimlik No"))
    phone = models.CharField(max_length=20, verbose_name=_("Telefon"))
    email = models.EmailField(verbose_name=_("E-posta"))
    address = models.TextField(verbose_name=_("Adres"))
    student_certificate = models.FileField(upload_to='applications/certificates/', verbose_name=_("Öğrenci Belgesi"))
    motivation = models.TextField(verbose_name=_("Motivasyon"))
    important_project_order = models.JSONField(verbose_name=_("Önemli Projeler Sıralaması"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Başvuru Tarihi"))

    class Meta:
        verbose_name = _("Başvuru")
        verbose_name_plural = _("Başvurular")

    def __str__(self):
        return self.full_name


class HeroSlider(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Başlık"))
    subtitle = models.CharField(max_length=300, blank=True, verbose_name=_("Alt Başlık"))
    image = models.ImageField(upload_to='hero_sliders/', verbose_name=_("Görsel"))
    is_active = models.BooleanField(default=True, verbose_name=_("Aktif mi?"))
    link = models.URLField(blank=True, null=True, verbose_name="Tıklanabilir Link")

    class Meta:
        verbose_name = _("Ana Slider")
        verbose_name_plural = _("Ana Sliderlar")

    def __str__(self):
        return self.title


class InfographicStep(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Başlık"))
    description = models.TextField(verbose_name=_("Açıklama"))
    icon = models.ImageField(upload_to="infographic/", verbose_name=_("İkon"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Sıra"))
    is_active = models.BooleanField(default=True, verbose_name=_("Aktif mi?"))

    class Meta:
        ordering = ['order']
        verbose_name = _("Başvuru Süreci Adımı")
        verbose_name_plural = _("Başvuru Süreci Adımları")

    def __str__(self):
        return self.title

class MenuItem(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Başlık"))
    url = models.CharField(max_length=255, blank=True, verbose_name=_("Bağlantı (URL)"))
    is_dropdown = models.BooleanField(default=False, verbose_name=_("Açılır Menü mü?"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Sıra"))
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children', verbose_name=_("Üst Menü"))

    class Meta:
        ordering = ['order']
        verbose_name = _("Menü")
        verbose_name_plural = _("Menüler")

    def __str__(self):
        return self.title

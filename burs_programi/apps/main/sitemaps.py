from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from apps.main.models import ScholarshipProgram
from apps.news.models import NewsArticle
from apps.stories.models import Story

# Ana ve statik sayfalar
class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'monthly'

    def items(self):
        return ['home', 'application_form', 'testimonials', 'scholarship_program_list', 'news_list']

    def location(self, item):
        return reverse(item)

# Dinamik: burs programları
class ScholarshipSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return ScholarshipProgram.objects.all()

    def location(self, obj):
        return reverse('scholarship_program_detail', args=[obj.slug])

# Dinamik: haberler
class NewsSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.6

    def items(self):
        return NewsArticle.objects.all()

    def location(self, obj):
        return reverse('news_detail', args=[obj.slug])

# Dinamik: başarı hikayeleri
class StorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return Story.objects.all()

    def location(self, obj):
        return reverse('story_detail', args=[obj.slug])

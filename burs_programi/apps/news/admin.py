from modeltranslation.admin import TranslationAdmin
from .models import NewsArticle, NewsCategory
from django.contrib import admin
from .translation import *

@admin.register(NewsCategory)
class NewsCategoryAdmin(TranslationAdmin):
    list_display = ('name',)

@admin.register(NewsArticle)
class NewsArticleAdmin(TranslationAdmin):
    list_display = ('title', 'category', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category',)
    search_fields = ('title', 'content')

from modeltranslation.translator import translator, TranslationOptions
from .models import NewsCategory, NewsArticle

class NewsCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

class NewsArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)

translator.register(NewsCategory, NewsCategoryTranslationOptions)
translator.register(NewsArticle, NewsArticleTranslationOptions)

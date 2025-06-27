from modeltranslation.translator import register, TranslationOptions
from .models import Interview, Story

@register(Interview)
class InterviewTranslationOptions(TranslationOptions):
    fields = ('title', 'video_url')

@register(Story)
class StoryTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
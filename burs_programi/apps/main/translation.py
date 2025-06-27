# apps/main/translation.py

from modeltranslation.translator import register, TranslationOptions
from .models import ScholarshipProgram, InfographicStep, HeroSlider, FAQ, MenuItem

@register(ScholarshipProgram)
class ScholarshipProgramTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(InfographicStep)
class InfographicStepTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(HeroSlider)
class HeroSliderTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle')

@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer',)

@register(MenuItem)
class MenuItemTranslationOptions(TranslationOptions):
    fields = ('title',)

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Story, Interview, Testimonial

from . import translation

@admin.register(Story)
class StoryAdmin(TranslationAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Interview)
class InterviewAdmin(TranslationAdmin):
    list_display = ('title',)
    search_fields = ('title', 'video_url')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'is_featured')
    list_filter = ('is_featured',)
    search_fields = ('name', 'surname', 'tag')

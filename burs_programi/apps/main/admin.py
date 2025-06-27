from . import translation
from django.contrib import admin
from .models import ScholarshipProgram, FAQ, HeroSlider, Application, MenuItem
from django.utils.translation import get_language
from .forms import ScholarshipProgramAdminForm
from modeltranslation.admin import TranslationAdmin


@admin.register(HeroSlider)
class HeroSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'link','is_active')
    list_filter = ('is_active',)


class FAQInline(admin.TabularInline):
    model = FAQ
    extra = 1

@admin.register(ScholarshipProgram)
class ScholarshipProgramAdmin(admin.ModelAdmin):
    form = ScholarshipProgramAdminForm
    list_display = ('title', 'tag')
    search_fields = ('title', 'tag')
    inlines = [FAQInline]

    def get_prepopulated_fields(self, request, obj=None):

        lang = get_language()
        return {'slug': (f'title_{lang}',)}

@admin.register(FAQ)
class FAQAdmin(TranslationAdmin):
    list_display = ('question', 'scholarship_program')
    search_fields = ('question',)
    list_filter = ('scholarship_program',)

from .models import InfographicStep
@admin.register(InfographicStep)
class InfographicStepAdmin(TranslationAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    list_filter = ('is_active',)

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'identity_number', 'email', 'phone', 'created_at')
    search_fields = ('full_name', 'identity_number', 'email')
    readonly_fields = ('created_at',)


@admin.register(MenuItem)
class MenuItemAdmin(TranslationAdmin):
    list_display = ('title', 'url', 'is_dropdown', 'parent', 'order')
    list_filter = ('is_dropdown', 'parent')
    search_fields = ('title',)
    ordering = ('order',)

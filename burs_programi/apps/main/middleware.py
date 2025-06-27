from django.utils import translation
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

class ForceLocaleFromURLMiddleware(MiddlewareMixin):
    def process_request(self, request):
        lang = translation.get_language_from_path(request.path_info)
        if lang and lang in dict(settings.LANGUAGES):
            translation.activate(lang)
            request.LANGUAGE_CODE = lang

# apps/main/templatetags/menu_tags.py
from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()

@register.filter
def resolve_url(value):
    if not value:
        return '#'

    if value.startswith('/'):
        return value

    parts = value.strip().split()
    url_name = parts[0]
    args = parts[1:]

    try:
        return reverse(url_name, args=args)
    except NoReverseMatch:
        return value


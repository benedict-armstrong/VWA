from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='poster_url')
@stringfilter
def poster_url(x, y):
    return "ben"
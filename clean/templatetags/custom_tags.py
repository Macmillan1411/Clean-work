#create a patners.html 
from django import template

register = template.Library()

@register.simple_tag
def include_partners_section():
    return 'partners.html'


@register.simple_tag
def include_our_best_services():
    return 'our_best_services.html'


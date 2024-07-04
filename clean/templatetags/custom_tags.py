#create a patners.html 
from django import template

register = template.Library()

@register.simple_tag
def include_partners_section():
    return 'partners.html'

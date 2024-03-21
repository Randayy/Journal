
from django import template

register = template.Library()

@register.filter
def add_placeholder(field, placeholder):
    field.field.widget.attrs.update({'placeholder': placeholder})
    return field

@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)
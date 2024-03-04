
from django import template

register = template.Library()

@register.filter
def add_placeholder(field, placeholder):
    field.field.widget.attrs.update({'placeholder': placeholder})
    return field
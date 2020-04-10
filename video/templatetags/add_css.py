# Źródło: https://stackoverflow.com/questions/25090735/register-custom-filter-in-django

from django import template

register = template.Library()


@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={'class': css})

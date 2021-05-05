from django import template

register = template.Library()


@register.filter
def filter_capitals(value):
    print(value)
    return "test filter"

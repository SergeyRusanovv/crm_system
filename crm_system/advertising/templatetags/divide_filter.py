from django import template

register = template.Library()


@register.simple_tag(name="divide")
def divide(value, arg):
    """Кастомный тэг для деления двух аргументов"""
    try:
        div = int(value) / int(arg)
        return round(div, 2)
    except (ValueError, ZeroDivisionError, TypeError):
        return "Не хватает данных для расчета!"

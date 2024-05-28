from django import template
register = template.Library()

@register.filter
def get_col(value):
    '''
    Divides the value; argument is the divisor.
    Returns empty string on any error.
    '''
    try:
        return value//100 + 1

    except: pass
    return ''

# taken from https://stackoverflow.com/questions/5848967/django-how-to-do-calculation-inside-the-template-html-page
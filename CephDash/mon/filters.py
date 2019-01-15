from django import template

register = template.Library()


@register.filter(name='sub')
def sub(value1, value2):
	return value1 - value2

@register.filter(name='usage')
def usage(value1, value2):
	percentage = value1/value2
	return round(percentage*100)

@register.filter(name='hbytes')
def hbytes(num):
    for x in ['bytes','KB','MB','GB']:
        if num < 1024.0:
            return "%3.1f%s" % (num, x)
        num /= 1024.0
    return "%3.1f%s" % (num, 'TB')


@register.filter(name='round')
def sub(value):
	return round(value, 2) 



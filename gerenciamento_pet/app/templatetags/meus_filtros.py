from django import template


# temos que registrar o template na library 
register = template.Library()


# aqui criamos o filtro
@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})

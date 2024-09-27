from django import template
from datetime import datetime
from main.models import Sotrudnic

register = template.Library()


@register.simple_tag()
def get_all_worker():
    return Sotrudnic.objects.all()

# @register.filter()
# def date_end_valed(date_end='10 июля 2024 г. 12:07',format='%d '):
#     date = datetime.strptime(date_end, format)
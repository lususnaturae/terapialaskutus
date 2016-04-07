from django import template
from ..models import Session

register = template.Library()

# Converts field value based on SESSION_TYPE_CHOICES to readable value
@register.simple_tag
def convert_sessiontype_to_readable_text(choice_string):
    return dict(Session.SESSION_TYPE_CHOICES)[choice_string]

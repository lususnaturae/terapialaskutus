from django import template
from ..models import KelaStatement
register = template.Library()

# Converts field value based on SESSION_TYPE_CHOICES to readable value
@register.simple_tag
def calc_totalrefund_of_kelastatement(kelastatament_pk):
    ic = KelaStatement.get_kelastatementcustomerlines(pk=kelastatament_pk)
    return ic['totalRefund']

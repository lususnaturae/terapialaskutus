from django import template
from ..models import InvoiceLineItem
register = template.Library()

# Converts field value based on SESSION_TYPE_CHOICES to readable value
@register.simple_tag
def calc_invoicetotal(invoice_pk):
    ic = InvoiceLineItem.get_invoicelineitems(pk=invoice_pk)
    return ic['invoiceTotal']

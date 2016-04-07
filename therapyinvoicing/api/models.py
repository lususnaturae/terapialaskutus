# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django import template
from django.db import models
from ..customerinvoicing.models import InvoiceLineItem
from ..kelainvoicing.models import KelaInvoiceLineItem

register = template.Library()


class TimeStampedModel(models.Model):
    """
        An Abstract base class that provides
        self updating ''created'' and ''modified'' fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class MonthlyRevenue(TimeStampedModel):
    """

    """
    year = models.CharField(max_length=4)
    month = models.CharField(max_length=2)
    customerRevenue = models.FloatField()
    kelaRevenue = models.FloatField()

    def get_totalrevenue(self):
        return self.customerRevenue + self.kelaRevenue

    def __str__(self):
        return self.year + "-" + self.month


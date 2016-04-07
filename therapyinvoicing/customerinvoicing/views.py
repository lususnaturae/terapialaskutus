import datetime
from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, RedirectView
from django.core.urlresolvers import reverse_lazy
from .models import Invoice, InvoiceLineItem
from braces.views import GroupRequiredMixin


class InvoiceListView(GroupRequiredMixin, ListView):
    """
    Show list of invoices ordered by '-date'
    """
    group_required = u'therapist'
    raise_exception = True
    queryset = Invoice.objects.order_by('-date')
    model = Invoice
    context_object_name = 'customer_invoices'

    def get_context_data(self, **kwargs):
        context = super(InvoiceListView, self).get_context_data(**kwargs)

        context['invoicesetpaiddatebuttontext'] = _('Merkitse maksetuksi')
        context['invoicelisttitle'] = _('Avoimet asiakaslaskut')
        context['customerinvoicablesessions'] = Invoice.get_customerinvoicablesessions()
        context['invoicelisttext'] = (_("Alla olevia asiakastapaamisia ei ole vielä laskutettu. " +
                                              "Asiakaskohtaiset laskut luodaan automaattisesti kun painat oheista nappia.")
                                              if context['customerinvoicablesessions'] != [] else
                                                _("EI LÖYDY LASKUTETTAVIA TAPAAMISIA")
                                             )
        return context


class InvoiceGenerateConfirmTemplateView(GroupRequiredMixin, TemplateView):
    """
    Show confirmation page for creating invoices to customers
    """
    group_required = u'therapist'
    raise_exception = True
    template_name = "customerinvoicing/invoice_generator_confirm.html"

    def get_context_data(self, **kwargs):
        context = super(InvoiceGenerateConfirmTemplateView, self).get_context_data(**kwargs)
        context['customerinvoicablesessions'] = Invoice.get_customerinvoicablesessions()
        context['invoicablesessionstitle'] = _("Tapaamiset valmiina laskutukseen asiakkailta")
        context['invoicablesessionstext'] = (_("Alla olevia asiakastapaamisia ei ole vielä laskutettu. " +
                                              "Asiakaskohtaiset laskut luodaan automaattisesti kun painat oheista nappia.")
                                              if context['customerinvoicablesessions'] != [] else
                                                _("EI LÖYDY LASKUTETTAVIA TAPAAMISIA")
                                             )
        context['backtoinvoicelistbuttontext'] = _("Palaa laskujen listaan")
        context['askconfirmationtext'] = _("Oletko varma, että haluat luoda laskut alla listatuille asiakkaille?")
        return context

    def get_success_url(self):
        return reverse_lazy('customerinvoicing:invoice_creator')


class InvoiceCreatorRedirectView(GroupRequiredMixin, RedirectView):
    """
    Redirect view to launch mehdod Invoice.create_invoices()
    """
    group_required = u'therapist'
    raise_exception = True
    permanent = False
    query_string = False
    pattern_name = 'customerinvoicing:invoice_list'

    def dispatch(self, *args, **kwargs):
        Invoice.create_invoices()
        return super(InvoiceCreatorRedirectView, self).dispatch(*args, **kwargs)


class InvoiceDetailView(GroupRequiredMixin, DetailView):
    """
    Show printable invoice
    """
    group_required = u'therapist'
    raise_exception = True
    model = Invoice
    context_object_name = 'customer_invoice'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(InvoiceDetailView, self).get_context_data(**kwargs)
        lineitemlist = InvoiceLineItem.get_invoicelineitems(pk=self.object.pk)
        context['invoicelineitems'] = lineitemlist['invoicelineitems']
        #context['lineitemcount'] = lineitemlist['lineitemcount']
        context['kelaRefundTotal'] = lineitemlist['kelaRefundTotal']
        context['invoiceTotal'] = lineitemlist['invoiceTotal']
        context['invoiceTotalWithoutKelaRefund'] = lineitemlist['invoiceTotalWithoutKelaRefund']
        context['backtoinvoicelistbuttontext'] = _("Palaa laskujen listaan")
        context['invoiceduedate'] = self.object.date + datetime.timedelta(days=14)
        return context

    def get_success_url(self):
        return reverse_lazy('customerinvoicing:invoice_list')

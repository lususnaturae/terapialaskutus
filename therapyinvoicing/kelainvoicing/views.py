
from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import CompanyProfile, KelaContactProfile
from .models import KelaStatement, KelaInvoice
from django.utils import timezone
from therapyinvoicing.kelainvoicing.forms import KelaStatementUpdateForm, KelaContactProfileUpdateForm
from braces.views import GroupRequiredMixin


class KelaContactProfileUpdateView(GroupRequiredMixin, UpdateView):
    """
    Show KelaContactProfile form
    """
    group_required = u'therapist'
    raise_exception = True
    model = KelaContactProfile
    form_class = KelaContactProfileUpdateForm

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(KelaContactProfileUpdateView, self).get_context_data(**kwargs)
        context['kelacontactprofileupdatetitletext'] = _("Muokkaa Kelan yhteystietoja")
        context['savebuttontext'] = _("Tallenna yhteystiedot")
        context['backtokelastatementlistbuttontext'] = _("Palaa tilitysten listaan")
        return context

    def get_success_url(self):
        return reverse_lazy('kelainvoicing:kelastatement_list')


class KelaStatementListView(GroupRequiredMixin, ListView):
    """
    Shows list of KelaStatement
    """
    group_required = u'therapist'
    raise_exception = True
    queryset = KelaStatement.objects.order_by('-date')
    model = KelaStatement
    context_object_name = 'kelastatement_list'

    def get_context_data(self, **kwargs):
        context = super(KelaStatementListView, self).get_context_data(**kwargs)

        context['createkelastatementbuttontext'] = _("Luo uusi tilitys Kelalle")
        context['kelastatmentlisttitle'] = _("Kelan tilitykset")
        context['kelastatementdeletebuttontext'] = _("Poista tilitys")

        # KelaContactProfile information
        context['kelacontactprofilecardtitle'] = _("Kelan laskutuksen yhteystiedot")
        context['kelacontactprofileupdatebuttontext'] = _("Muokkaa Kelan yhteystietoja")
        context['kelacontactprofile'] = KelaContactProfile.get_or_create_kelacontactprofile()

        # Invoicable sessions
        context['stbi'] = KelaStatement.get_kelainvoicablesessions()
        context['invoicablesessionstitle'] = _("Kelalle tilittämättömät tapaamiset")
        context['invoicablesessionstext'] = (_("Alla olevia asiakastapaamisia ei ole vielä tilitetty Kelalle. " +
                                              "Asiakaskohtaiset laskut Kelalle luodaan automaattisesti kun tallennat tilityslomakkeen.")
                                              if context['stbi'] != [] else
                                                _("EI LÖYDY LASKUTETTAVIA TAPAAMISIA")
                                             )


        return context


class KelaStatementDetailView(GroupRequiredMixin, DetailView):
    """
    Show details of single KelaStatement
    """
    group_required = u'therapist'
    raise_exception = True
    model = KelaStatement

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(KelaStatementDetailView, self).get_context_data(**kwargs)
        ic = KelaStatement.get_kelastatementcustomerlines(pk=self.object.pk)
        context['invoicablecustomers'] = ic['invoicablecustomers']
        context['totalRefund'] = ic['totalRefund']
        context['count'] = ic['count']
        context['backtokelastatementlistbuttontext'] = _("Palaa tilitysten listaan")
        return context

    def get_success_url(self):
        return reverse_lazy('customers:kelastatement_generate')


class KelaStatementCreateView(GroupRequiredMixin, CreateView):
    """
    Show KelaStatement form
    """
    group_required = u'therapist'
    raise_exception = True
    model = KelaStatement
    form_class = KelaStatementUpdateForm

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(KelaStatementCreateView, self).get_context_data(**kwargs)
        context['backtokelastatementlistbuttontext'] = _("Palaa tilitysten listaan")
        context['savebuttontext'] = _("Tallenna tilitys")
        # Invoicable sessions
        context['stbi'] = KelaStatement.get_kelainvoicablesessions()
        context['invoicablesessionstitle'] = _("Kelalle tilittämättömät tapaamiset")
        context['invoicablesessionstext'] = (_("Alla olevia asiakastapaamisia ei ole vielä tilitetty Kelalle. " +
                                              "Asiakaskohtaiset laskut Kelalle luodaan automaattisesti kun tallennat tilityslomakkeen.")
                                              if context['stbi'] != [] else
                                                _("EI LÖYDY LASKUTETTAVIA TAPAAMISIA")
                                             )
        return context

    def get_initial(self):
        q = CompanyProfile.objects.first()
        #find max ref
        if KelaStatement.objects.all().exists():
            kpobj = KelaStatement.objects.all().order_by('-orderno')[:1].get()
            maxnum = int(kpobj.orderno) + 1
            t=1
        else:
            #if no invoices set max number to 1000
            maxnum = '12'
        return {
            'date': timezone.now(),
            'companyName': q.companyName,
            'firstName': q.firstName,
            'lastName': q.lastName,
            'address': q.address,
            'zipCode': q.zipCode,
            'city': q.city,
            'telephone': q.telephone,
            'email': q.email,
            'vatId': q.vatId,
            'iban': q.iban,
            'bic': q.bic,
            'serviceproviderType': q.serviceproviderType,
            'invoiceRefType': q.invoiceRefType,
            'orderno': maxnum,
            'taxAdvanceType': q.taxAdvanceType,
            'taxAdvanceExplanation': ""}

    def get_success_url(self):
        return reverse_lazy('kelainvoicing:kelastatement_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form, *args, **kwargs):
        # save form first to get object needed in ForeignKeys
        self.object = form.save(commit=False)
        self.object.save()
        KelaStatement.create_kelainvoices(pk=self.object.pk)
        return super(KelaStatementCreateView, self).form_valid(form)


class KelaStatementUpdateView(GroupRequiredMixin, UpdateView):
    group_required = u'therapist'
    raise_exception = True

    model = KelaStatement
    form_class = KelaStatementUpdateForm
    context_object_name = 'kelastatement'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(KelaStatementUpdateView, self).get_context_data(**kwargs)
        context['backtokelastatementlistbuttontext'] = _("Palaa tilitysten listaan")
        context['savebuttontext'] = _("Tallenna tilitys")
        return context

    def get_success_url(self):
        return reverse_lazy('kelainvoicing:kelastatement_detail', kwargs={'pk': self.object.pk})


class KelaStatementDeleteView(GroupRequiredMixin, DeleteView):
    group_required = u'therapist'
    raise_exception = True
    model = KelaStatement

    def get_success_url(self):
        return reverse_lazy('customers:kelastatement_list')


class KelaInvoiceDetailView(GroupRequiredMixin, DetailView):
    group_required = u'therapist'
    raise_exception = True
    model = KelaInvoice
    context_object_name = 'kelainvoice'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context

        context = super(KelaInvoiceDetailView, self).get_context_data(**kwargs)
        dd = KelaInvoice.get_kelainvoicelineitems(pk=self.object.pk)
        #TODO: create function to get kelainvoicelineitems related to this invoice
        slist = dd['sessions']
        slist1 = []
        slist2 = []
        slist3 = []
        emptyline = {
                    'date': "",
                    'sessionType': "",
                    'sessionprice': "",
                    'sessionpriceKelaRefund': "",
                    'linenum': ""
                }
        slength = len(slist)
        for x in range(0, 20):
            if x < slength:
                if x < 10:
                    slist1.append(slist.pop(0))
                else:
                    slist2.append(slist.pop(0))
            else:
                if x < 10:
                    slist1.append(emptyline)
                else:
                    slist2.append(emptyline)
        for x in range(0,10):
            s1 = slist1.pop(0)
            s2 = slist2.pop(0)
            slist3.append({
                'date1': s1['date'],
                'sessionType1': s1['sessionType'],
                    'sessionprice1': s1['sessionprice'],
                    'sessionpriceKelaRefund1': s1['sessionpriceKelaRefund'],
                'date2': s2['date'],
                'sessionType2': s2['sessionType'],
                    'sessionprice2': s2['sessionprice'],
                    'sessionpriceKelaRefund2': s2['sessionpriceKelaRefund'],
            })
        context['slist'] = slist3
        context['backtokelastatementlistbuttontext'] = _('Palaa tilitykseen')
        context['sessioncount'] = dd['sessioncount']
        context['kelaRefundTotal'] = dd['kelaRefundTotal']
        return context

    def get_success_url(self):
        return reverse_lazy('customers:kelastatement_generate')

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Customer, Session, CompanyProfile
from therapyinvoicing.customers.forms import  CustomerUpdateForm, SessionUpdateForm, CompanyProfileUpdateForm
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404
from django.utils import timezone
from braces.views import GroupRequiredMixin


class CustomerListView(GroupRequiredMixin, ListView):
    """
    Shows all customers
    """
    group_required = u'therapist'
    raise_exception = True
    queryset = Customer.objects.all().order_by('lastName', 'firstName')

    def get_context_data(self, **kwargs):
        context = super(CustomerListView, self).get_context_data(**kwargs)
        context['createnewcustomer'] = _("Luo uusi asiakas")
        return context


class CustomerDetailView(GroupRequiredMixin, DetailView):
    """
    Shows detail of selected customer and list of Sessions linked to Customer
    """
    group_required = u'therapist'
    raise_exception = True
    model = Customer

    fields = ['firstName',  'lastName', 'ssn', 'address', 'zipCode', 'city',  'telephone', 'email', 'status',
              'therapyCategory', 'sessionprice', 'sessionpriceKelaRefund']

    def get_context_data(self, **kwargs):
        context = super(CustomerDetailView, self).get_context_data(**kwargs)
        cc = get_object_or_404(Customer, pk=self.kwargs.get('pk'))
        context['customer'] = cc
        context['contacttitle'] = _("Asiakkaan Yhteystiedot")
        context['addresstitle'] = _("Osoite")
        context['telephonetitle'] = _("Puhelinnumero")
        context['emailtitle'] = _("Sähköposti")
        context['ssntitle'] = _("Sosiaaliturvatunnus")
        context['pricingtitle'] = _("Hinnoittelu")
        context['sessionpricelabel'] = _("Terapiakäynnin hinta ")
        context['sessionpricekelarefundabel'] = _("Kelakorvaus terapiakäynnistä")
        context['sessioncosttocustomerlabel'] = _("Asiakkaan osuus terapiakäynnistä")
        context['pricingtitle'] = _("Asiakashinnoittelu")
        context['sessionlisttitle'] = _("Tapaamiset")
        context['customersessions'] = Session.objects.filter(customer=cc.id).order_by('-date').values()
        context['editbuttontext'] = _("Muokkaa asiakkaan tietoja")
        context['backtocustomerlistbuttontext'] = _("Palaa asiakaslistaan")
        context['addsessionbuttontext'] = _("Lisää uusi tapaaminen")
        return context


class CustomerUpdateView(GroupRequiredMixin, UpdateView):
    """
    Shows Customer update form
    """
    group_required = u'therapist'
    raise_exception = True
    model = Customer
    form_class = CustomerUpdateForm
    context_object_name = 'customer'

    def get_context_data(self, **kwargs):
        context = super(CustomerUpdateView, self).get_context_data(**kwargs)
        context['savebuttontext'] = _("Tallenna")
        context['backtocustomerlistbuttontext'] = _("Palaa tallentamatta")
        return context

    def get_success_url(self):
        return reverse_lazy('customers:customer_detail', kwargs={'pk': self.object.pk})


class CustomerCreateView(GroupRequiredMixin, CreateView):
    """
    Shows Customer Create form
    """
    group_required = u'therapist'
    raise_exception = True
    model = Customer
    form_class = CustomerUpdateForm

    def get_context_data(self, **kwargs):
        context = super(CustomerCreateView, self).get_context_data(**kwargs)
        context['savebuttontext'] = _("Tallenna")
        context['backtocustomerlistbuttontext'] = _("Palaa tallentamatta")
        return context

    def get_success_url(self):
        return reverse_lazy('customers:customer_list')


class CustomerDeleteView(GroupRequiredMixin, DeleteView):
    """
    Shows customer delete confirmation page
    """
    group_required = u'therapist'
    raise_exception = True
    model = Customer

    def get_success_url(self):
        return reverse_lazy('customers:customer_list')


class SessionListView(GroupRequiredMixin, ListView):
    """
    Shows list of Therapy Sessions
    """
    group_required = u'therapist'
    raise_exception = True
    model = Session
    fields = ['date',  'time',  'sessionDone']

    def get_queryset(self):
        self.customer = get_object_or_404(Customer, pk=self.kwargs.get('pk'))
        return Session.objects.filter(customer=self.customer)

    def get_context_data(self, **kwargs):
        context = super(SessionListView, self).get_context_data(**kwargs)
        context['customer'] = get_object_or_404(Customer, pk=self.kwargs.get('pk'))
        return context


class SessionDetailView(GroupRequiredMixin, DetailView):
    """
    Show details of single Therapy Session
    """
    group_required = u'therapist'
    raise_exception = True
    model = Session
    fields = ['date',  'time', 'sessionInvoiceType', 'kelaInvoiceType', 'sessionDone']

    def get_success_url(self):
        return reverse_lazy('customers:customer_detail', kwargs={'pk': self.customer.pk})


class SessionUpdateView(GroupRequiredMixin, UpdateView):
    """
    Shows Session Update form
    """
    group_required = u'therapist'
    raise_exception = True
    model = Session
    form_class = SessionUpdateForm
    context_object_name = 'customer_session'

    def get_context_data(self, **kwargs):
        context = super(SessionUpdateView, self).get_context_data(**kwargs)
        context['savebuttontext'] = _("Tallenna")
        context['backtocustomerdetailbuttontext'] = _("Palaa tallentamatta")

        return context

    def get_success_url(self):
        return reverse_lazy('customers:customer_detail', kwargs={'pk': self.object.customer.pk})


class SessionCreateView(GroupRequiredMixin, CreateView):
    """
    Shows Session Create form
    """
    group_required = u'therapist'
    raise_exception = True
    model = Session
    form_class = SessionUpdateForm


    def get_success_url(self):
        return reverse_lazy('customers:customer_detail', kwargs={'pk': self.object.customer.pk})

    def get_context_data(self, **kwargs):
        context = super(SessionCreateView, self).get_context_data(**kwargs)
        cobj = get_object_or_404(Customer, pk=self.kwargs.get('pk'))
        context['customer'] = cobj
        context['savebuttontext'] = _("Tallenna")
        context['backtocustomerdetailbuttontext'] = _("Palaa tallentamatta")
        return context

    # sets default values into form fields, e.g. gets price information from Customter
    def get_initial(self, **kwargs):
        q = get_object_or_404(Customer, pk=self.kwargs.get('pk'))
        return {
            'date': timezone.now(),
            'time': timezone.now(),
            'sessionInvoiceType': 'SINGLESESSION',
            'kelaInvoiceType': 'CANINVOICEKELA',
            'sessionType': 'YKSILÖ',
            'sessionprice': q.sessionprice,
            'sessionpriceKelaRefund': q.sessionpriceKelaRefund
        }

    def form_valid(self, form):
        form.instance.customer = get_object_or_404(Customer, pk=self.kwargs.get('pk'))
        return super(SessionCreateView, self).form_valid(form)


class SessionDeleteView(GroupRequiredMixin, DeleteView):
    """
    Shows Session delete confirmation page
    """
    group_required = u'therapist'
    raise_exception = True
    model = Session
    context_object_name = 'customer_session'
    success_url = reverse_lazy('customers:session_list')

    def get_context_data(self, **kwargs):
        context = super(SessionDeleteView, self).get_context_data(**kwargs)
        context['deleteconfirmationtitletext'] = _("Oletko varma, että halua poistaa oheisen asiakkaan tapaamisen?")
        context['deleteconfirmationbuttontext'] = _("Vahvista tapaamisen poistaminen")
        context['backtocustomerdetailbuttontext'] = _("Palaa poistamatta tapaamista")
        return context

    def get_success_url(self):
        return reverse_lazy('customers:customer_detail', kwargs={'pk': self.object.customer.pk})


class CompanyProfileDetailView(GroupRequiredMixin, DetailView):
    """
    Shows CompanyProfile detail page
    """
    group_required = u'therapist'
    raise_exception = True
    model = CompanyProfile
    fields = ['companyName', 'firstName', 'lastName', 'address', 'zipCode', 'city',  'telephone', 'email', 'vatId', 'iban', 'bic', 'serviceproviderType']

    context_object_name = 'companyprofile'

    # get companyprofile or create new if it does not exist
    def get_initial(self):
        cp = CompanyProfile.get_or_create_companyprofile()
        return cp

    def get_context_data(self, **kwargs):
        context = super(CompanyProfileDetailView, self).get_context_data(**kwargs)
        context['companyprofile'] = CompanyProfile.get_or_create_companyprofile()
        context['companyprofiletitle'] = _("Oman yrityksen tiedot")
        context['updatebuttontext'] = _("Muokkaa yrityksesi profiilia")
        context['backtocustomerlistbuttontext'] = _("Palaa asiakaslistaan")
        return context


class CompanyProfileUpdateView(GroupRequiredMixin, UpdateView):
    """
    Shows CompanyProfile Update form
    """
    group_required = u'therapist'
    raise_exception = True
    model = CompanyProfile
    form_class = CompanyProfileUpdateForm
    context_object_name = 'companyprofile'

    def get_context_data(self, **kwargs):
        context = super(CompanyProfileUpdateView, self).get_context_data(**kwargs)
        context['companyprofiletitle'] = _("Oman yrityksen tiedot")
        context['savebuttontext'] = _("Tallenna profiili")
        context['backtocompanyprofiledetailbuttontext'] = _("Palaa tallentamatta")
        return context

    # send the user back to companyprofile aftersuccessfull update
    def get_success_url(self):
        return reverse_lazy('customers:companyprofile_detail', kwargs={'pk': self.object.pk})


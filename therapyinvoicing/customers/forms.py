from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Customer, Session, CompanyProfile


class CustomerUpdateForm(forms.ModelForm):
    """
    Update Customer form
    Field enhancements:
    * therapyCategory uses forms.TypedChoiceField.
    """
    class Meta:
        model = Customer
        fields = ['status', 'firstName', 'lastName', 'additionalName', 'ssn', 'address', 'zipCode', 'city', 'telephone', 'email',

                  'therapyCategory', 'sessionprice', 'sessionpriceKelaRefund'
                # , 'statementpriceKela'
                  ]
        labels = {
            'firstName': _("Etunimi"),
            'additionalName': _("Muut etunimet"),
            'lastName': _("Sukunimi"),
            'ssn': _("Sosiaaliturvatunnus"),
            'address': _("Osoite"),
            'zipCode': _("Postinumero"),
            'city': _("Postitoimipaikka"),
            'telephone': _("Puhelin"),
            'email': _("Sähköposti"),
            'status': _("Aktiivinen asiakas?"),
            'therapyCategory': _("Terapialuokitus"),
            'sessionprice': _("Tapaamisen perushinta"),
            'sessionpriceKelaRefund': _("Kelan korvaus"),
            # 'statementpriceKela': _("Kelakorvaus lausunnosta"),
        }


    therapyCategory = forms.TypedChoiceField(
        label=Meta.labels['therapyCategory'],
        choices=Customer.THERAPY_CATEGORY_CHOICES,
        widget=forms.Select,

        required=True
    )


class CustomerCreateForm(forms.ModelForm):
    """
    Create Customer form.
    Field enhancements:
    * therapyCategory uses forms.TypedChoiceField.
    """
    class Meta:
        model = Customer
        fields = ['firstName', 'lastName', 'additionalName', 'ssn', 'address', 'zipCode', 'city', 'telephone', 'email',
                  'status',
                  'therapyCategory', 'sessionprice', 'sessionpriceKelaRefund']
        labels = {
            'firstName': _("Etunimi"),
            'additionalName': _("Muut etunimet"),
            'lastName': _("Sukunimi"),
            'ssn': _("Sosiaaliturvatunnus"),
            'address': _("Osoite"),
            'zipCode': _("Postinumero"),
            'city': _("Postitoimipaikka"),
            'telephone': _("Puhelin"),
            'email': _("Sähköposti"),
            'status': _("Aktiivinen asiakas?"),
            'therapyCategory': _("Terapialuokitus"),
            'sessionprice': _("Tapaamisen perushinta"),
            'sessionpriceKelaRefund': _("Kelan korvaus"),
        }


    therapyCategory = forms.TypedChoiceField(
        label=Meta.labels['therapyCategory'],
        choices=Customer.THERAPY_CATEGORY_CHOICES,
        widget=forms.Select,


        required=True
    )


class SessionUpdateForm(forms.ModelForm):
    """
    Update Customer form.
    Field enhancements:
    * time uses forms.TimeField with format '%H:%M'
    * sessionInvoiceType uses forms.TypedChoiceField choices from Session.SESSION_INVOICE_CHOICES
    * kelaInvoiceType uses forms.TypedChoiceField choices from Session.KELAINVOICABLE_CHOICES
    * sessionType uses forms.TypedChoiceField choices from Session.SESSION_TYPE_CHOICES
    """
    class Meta:
        model = Session
        fields = [
            'date',
            'time',
             'sessionType',
            'sessionInvoiceType',
            'kelaInvoiceType',
            'sessionprice',
            'sessionpriceKelaRefund',
            'sessionDone'

        ]
        labels = {
            'date': _("Tapaamispäivä"),
            'time': _("Tapaamisaika"),
            'sessionType': _("Tapaamisen tyyppi"),
            'sessionInvoiceType': _("Tapaamisen laskutus"),
            'kelaInvoiceType': _("Maksaako Kela osan asiakkaan kustannuksista?"),
            'sessionprice': _("Tapaamisen hinta"),
            'sessionpriceKelaRefund': _("Kelan maksama osuus tapaamisen hinnasta"),
            'sessionDone': _("Onko tapaaminen pidetty?")

        }

    time = forms.TimeField(
        label=Meta.labels['time'],
        widget=forms.TimeInput(format='%H:%M'),

        required=True
    )

    sessionInvoiceType = forms.TypedChoiceField(
        label=Meta.labels['sessionInvoiceType'],
        choices=Session.SESSION_INVOICE_CHOICES,
        widget=forms.Select,

        required=True
    )
    kelaInvoiceType = forms.TypedChoiceField(
        label=Meta.labels['kelaInvoiceType'],
        choices=Session.KELAINVOICABLE_CHOICES,
        widget=forms.Select,

        required=True
    )
    sessionType = forms.TypedChoiceField(
        label=Meta.labels['sessionType'],
        choices=Session.SESSION_TYPE_CHOICES,
        widget=forms.Select,

        required=True
    )


class CompanyProfileUpdateForm(forms.ModelForm):
    """
    CustomerProfile update form.
    Field enhancements:
    * time uses forms.TimeField with format '%H:%M'
    * serviceproviderType uses forms.TypedChoiceField choices from CompanyProfile.SERVICEPROVIDER_TYPE_CHOICES
    * invoiceRefType uses forms.TypedChoiceField choices from CompanyProfile.INVOICEREF_TYPE_CHOICES
    * taxAdvanceType uses forms.TypedChoiceField choices from CompanyProfile.TAX_ADVANCE_COLLECTION_TYPE_CHOICES
    """
    class Meta:
        model = CompanyProfile
        fields = [
            'companyName',
            'firstName',
            'additionalName',
            'lastName',
            'address',
            'zipCode',
            'city',
            'country',
            'telephone',
            'email',
            'vatId',
            'iban',
            'bic',
            'serviceproviderType',
            'invoiceRefType',
            'taxAdvanceType'


        ]
        labels = {
            'companyName': _("Oman yrityksen nimi"),
            'firstName': _("Etunimi"),
            'additionalName': _("Muut etunimet"),
            'lastName': _("Sukunimi"),
            'address': _("Osoite"),
            'zipCode': _("Postinumero"),
            'city': _("Postitoimipaikka"),
            'country': _("Maa"),
            'telephone': _("Puhelin"),
            'email': _("Sähköposti"),
            'vatId': _("Y-tunnus/Henkilötunnus"),
            'iban': _("Pankkitili (IBAN)"),
            'bic': _("Pankkiyhteys (BIC)"),
            'serviceproviderType': _("Palveluntarjoajatyyppi"),
            'invoiceRefType': _("Kelan laskun viitetyyppi"),
            'taxAdvanceType': _("Ennakinpidätysperuste")

        }

    serviceproviderType = forms.TypedChoiceField(
        label=Meta.labels['serviceproviderType'],
        choices=CompanyProfile.SERVICEPROVIDER_TYPE_CHOICES,
        widget=forms.Select,

        required=True
    )
    invoiceRefType = forms.TypedChoiceField(
        label=Meta.labels['invoiceRefType'],
        choices=CompanyProfile.INVOICEREF_TYPE_CHOICES,
        widget=forms.Select,

        required=True
    )
    taxAdvanceType = forms.TypedChoiceField(
        label=Meta.labels['taxAdvanceType'],
        choices=CompanyProfile.TAX_ADVANCE_COLLECTION_TYPE_CHOICES,
        widget=forms.Select,

        required=True
    )

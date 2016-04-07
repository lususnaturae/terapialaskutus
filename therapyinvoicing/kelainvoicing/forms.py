from django import forms
from .models import KelaContactProfile, KelaStatement
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.core.urlresolvers import reverse_lazy


class KelaStatementUpdateForm(forms.ModelForm):
    class Meta:
        model = KelaStatement
        fields = ['date',
              'companyName',
              'firstName',
              'lastName',
              'address',
              'zipCode',
              'city',
              'telephone',
              'email',
              'vatId',
              'iban',
              'bic',
              'serviceproviderType',
              'invoiceRefType',
              'orderno',
              'taxAdvanceType',
              'taxAdvanceExplanation']

        labels = {
            'date': _("Tilityspäivä"),
              'companyName': _("Kuntoutuspalvelutuottajan nimi"),
              'firstName': _("Terapeutin etunimi"),
              'lastName': _("Terapeutin sukunimi"),
              'address': _("Kuntoutuspalvelutuottajan katuosoite"),
              'zipCode': _("Kuntoutuspalvelutuottajan postinumero"),
              'city': _("Kuntoutuspalvelutuottajan Postitoimipaikka"),
              'telephone': _("Puhelinnumero"),
              'email': _("Sähköposti"),
              'vatId': _("Y-tunnus/Henkilötunnus"),
              'iban': _("Maksuosoite: IBAN-tilinumero"),
              'bic': _("BIC-pankkitunniste"),
              'serviceproviderType': _("Palveluntuottajan tyyppi"),
              'invoiceRefType': _("Tilitysnumeron tyyppi"),
              'orderno': _("Tilitysnumero"),
              'taxAdvanceType': _("Ennakonpidätysperuste"),
              'taxAdvanceExplanation': _("Ennakonpidätyksen selite")

        }
    serviceproviderType = forms.TypedChoiceField(
        label=Meta.labels['serviceproviderType'],
        choices=KelaStatement.SERVICEPROVIDER_TYPE_CHOICES,
        widget=forms.RadioSelect,

        required=True
    )
    invoiceRefType = forms.TypedChoiceField(
        label=Meta.labels['invoiceRefType'],
        choices=KelaStatement.INVOICEREF_TYPE_CHOICES,
        widget=forms.RadioSelect,

        required=True
    )
    taxAdvanceType = forms.TypedChoiceField(
        label=Meta.labels['taxAdvanceType'],
        choices=KelaStatement.TAX_ADVANCE_COLLECTION_TYPE_CHOICES,
        widget=forms.RadioSelect,

        required=True
    )

    def __init__(self, *args, **kwargs):
        super(KelaStatementUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'

        self.helper.form_action = reverse_lazy('customers:customer_create')
        self.helper.layout = Layout(
            'date',
              'companyName',
              'firstName',
              'lastName',
              'address',
              'zipCode',
              'city',
              'telephone',
              'email',
              'vatId',
              'iban',
              'bic',
              'serviceproviderType',
              'invoiceRefType',
              'orderno',
              'taxAdvanceType',
              'taxAdvanceExplanation',
            Submit("submit", _("Tallenna"), css_class="btn btn-primary btn-sm"),
        )


class KelaContactProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = KelaContactProfile
        fields = [
            'legalName',
            'firstName',
            'additionalName',
            'lastName',
            'address',
            'zipCode',
            'city',
            'country',
            'telephone',
            'email']

        labels = {
              'legalName': _("Kelan toimiston nimi"),
              'firstName': _("Yhteyshenkilön etunimi"),
              'lastName': _("Yhteyshenkilön sukunimi"),
              'address': _("Kelan laskutuksen postiosoite"),
              'zipCode': _("Kelan laskutuksen postinumero"),
              'city': _("Kelan laskutuksen postitoimipaikka"),
              'telephone': _("Puhelinnumero"),
              'email': _("Sähköposti"),


        }





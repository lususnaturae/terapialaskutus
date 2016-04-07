from selenium.webdriver.common.by import By

#Main page for anonymous users
class MainPageAnonymousUsersLocators(object):
    """

    """
    MENU_DROPDOWN = (By.ID, 'dropdownMenu1')
    LOGIN_NAVITEM = (By.ID, 'log-in-link')


#Main page for users that has been logged in
class MainPageLoggedInUsersLocators(object):
    """

    """
    MENU_DROPDOWN = (By.ID, 'dropdownMenu1')
    LOGIN_NAVITEM = (By.ID, 'log-in-link')
    ALERTMESSAGE = (By.CLASS_NAME, 'alert-danger')
    MYPROFILE_BUTTON = (By.ID, 'myprofile-link')
    LOGOUT_NAVITEM = (By.ID, 'logout-link')

    CUSTOMER_NAVITEM = (By.ID, 'customersnavitem')
    KELAINVOICING_NAVITEM = (By.ID, 'kelainvoicingnavitem')
    CUSTOMERINVOICING_NAVITEM = (By.ID, 'customerinvoicingnavitem')
    OWNCOMPANY_NAVITEM = (By.ID, 'owncompanynavitem')


class LoginPageLocators(object):
    """

    """
    MENU_DROPDOWN = (By.ID, 'dropdownMenu1')
    LOGIN_NAVITEM = (By.ID, 'log-in-link')
    LOGIN_FORM = (By.ID, 'div_id_login')
    USERNAME_FIELD = (By.ID, 'id_login')
    PASSWORD_FIELD = (By.ID, 'id_password')
    REMEMBERME_CHECKBOX = (By.ID, 'id_remember')
    SIGNIN_BUTTON = (By.ID, 'sign-in-button')
    ALERTMESSAGE = (By.CLASS_NAME, 'alert-danger')
    MYPROFILE_BUTTON = (By.ID, 'myprofile-link')
    LOGOUT_NAVITEM = (By.ID, 'logout-link')

    CUSTOMER_NAVITEM = (By.ID, 'customersnavitem')
    KELAINVOICING_NAVITEM = (By.ID, 'kelainvoicingnavitem')
    CUSTOMERINVOICING_NAVITEM = (By.ID, 'customerinvoicingnavitem')
    OWNCOMPANY_NAVITEM = (By.ID, 'owncompanynavitem')
    INVOICING_NAVITEM = (By.ID, 'invoicingnavitem')


class KelaStatementListPageLocators(object):
    """

    """

    KELASTATEMENTCREATE_BUTTON = (By.ID, 'kelastatement-create-button')
    KELASTATEMENTDETAIL_LINK = (By.ID, 'kelastatment-detail-link')
    KELACONTACTPROFILEUPDATE_BUTTON = (By.ID, 'kelacontactprofile-update-button')


class KelaStatementFormPageLocators(object):
    """

    """
    DATE_FIELD = (By.ID, 'id_date')
    COMPANYNAME_FIELD = (By.ID, 'id_companyName')
    FIRSTNAME_FIELD = (By.ID, 'id_firstName')
    LASTNAME_FIELD = (By.ID, 'id_lastName')
    ADDITIONALNAME_FIELD = (By.ID, 'id_additionalName')
    SSN_FIELD = (By.ID, 'id_ssn')
    ADDRESS_FIELD = (By.ID, 'id_address')
    ZIPCODE_FIELD = (By.ID, 'id_zipCode')
    CITY_FIELD = (By.ID, 'id_city')
    TELEPHONE_FIELD = (By.ID, 'id_telephone')
    EMAIL_FIELD = (By.ID, 'id_email')
    VATID_FIELD = (By.ID, 'id_vatId')
    IBAN_FIELD = (By.ID, 'id_iban')
    BIC_FIELD = (By.ID, 'id_bic')
    SERVICEPROVIDERTYPE_FIELD = (By.NAME, 'serviceproviderType')
    INVOICEREFTYPE_FIELD = (By.NAME, 'invoiceRefType')
    TAXADVANCETYPE_FIELD = (By.NAME, 'taxAdvanceType')
    ORDERNO_FIELD = (By.ID, 'id_orderno')
    TAXADVANCEEXPLANATION_FIELD = (By.ID, 'id_taxAdvanceExplanation')

    KELASTATEMENT_SAVE_BUTTON = (By.ID, 'kelastatement-save-button')
    KELASTATEMENTLIST_BUTTON = (By.ID, 'kelastatementlist-button')


class KelaStatementDetailPageLocators(object):
    """

    """
    KELASTATEMENTLIST_BUTTON = (By.ID, 'kelastatementlist-button')


class KelaInvoiceDetailPageLocators(object):
    """

    """
    KELASTATEMENTDETAIL_BUTTON = (By.ID, 'kelastatementdetail-button')


class KelaContactProfileUpdatePageLocators(object):
    """

    """
    KELACONTACTPROFILE_SAVE_BUTTON = (By.ID, 'companyprofile-save-button')



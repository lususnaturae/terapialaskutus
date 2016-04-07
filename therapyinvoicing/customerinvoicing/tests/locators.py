from selenium.webdriver.common.by import By


class MainPageAnonymousUsersLocators(object):

    MENU_DROPDOWN = (By.ID, 'dropdownMenu1')
    LOGIN_NAVITEM = (By.ID, 'log-in-link')


class MainPageLoggedInUsersLocators(object):

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


class InvoiceListPageLocators(object):

    INVOICECREATE_BUTTON = (By.ID, 'generateinvoice-button')
    INVOICEDETAIL_LINK = (By.ID, 'invoice-link')


class GenerateInvoicePageLocators(object):

    CONFIRMINVOICECREATE_BUTTON = (By.ID, 'confirminvoicegeneration-button')
    INVOICELIST_BUTTON = (By.ID, 'invoicelist-button')


class InvoiceDetailPageLocators(object):

    INVOICELIST_BUTTON = (By.ID, 'invoicelist-button')



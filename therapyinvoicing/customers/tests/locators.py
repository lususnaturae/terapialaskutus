from selenium.webdriver.common.by import By

#Main page for anonymous users
class MainPageAnonymousUsersLocators(object):

    MENU_DROPDOWN = (By.ID, 'dropdownMenu1')
    LOGIN_NAVITEM = (By.ID, 'log-in-link')


#Main page for users that has been logged in
class MainPageLoggedInUsersLocators(object):

    MENU_DROPDOWN = (By.ID, 'dropdownMenu1')
    LOGIN_NAVITEM = (By.ID, 'log-in-link')
    ALERTMESSAGE = (By.CLASS_NAME, 'alert-danger')
    MYPROFILE_BUTTON = (By.ID, 'myprofile-link')
    LOGOUT_NAVITEM = (By.ID, 'logout-link')
    CUSTOMER_NAVITEM = (By.ID, 'customersnavitem')
    INVOICING_NAVITEM = (By.ID, 'invoicingnavitem')


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
    INVOICING_NAVITEM = (By.ID, 'invoicingnavitem')


class CustomerListPageLocators(object):

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
    INVOICING_NAVITEM = (By.ID, 'invoicingnavitem')
    CREATECUSTOMER_LINK = (By.ID, 'customer-create-customer')
    TESTCUSTOMER_CARD = (By.LINK_TEXT, 'testlastname, testfirstname')


class CustomerFormPageLocators(object):

    FIRSTNAME_FIELD = (By.ID, 'id_firstName')
    LASTNAME_FIELD = (By.ID, 'id_lastName')
    ADDITIONALNAME_FIELD = (By.ID, 'id_additionalName')
    SSN_FIELD = (By.ID, 'id_ssn')
    ADDRESS_FIELD = (By.ID, 'id_address')
    ZIPCODE_FIELD = (By.ID, 'id_zipCode')
    CITY_FIELD = (By.ID, 'id_city')
    TELEPHONE_FIELD = (By.ID, 'id_telephone')
    EMAIL_FIELD = (By.ID, 'id_email')
    STATUS_FIELD = (By.ID, 'id_status')
    THERAPYCATEGORY_FIELD = (By.ID, 'id_therapyCategory')
    SESSIONPRICE_FIELD = (By.ID, 'id_sessionprice')
    SESSIONPRICEKELAREFUND_FIELD = (By.ID, 'id_sessionpriceKelaRefund')
    # STATEMENTPRICEKELA_FIELD = (By.ID, 'id_statementpriceKela')
    SAVE_BUTTON = (By.ID, 'customersave-button')


class CustomerDetailPageLocators(object):

    CUSTOMEREDIT_BUTTON = (By.ID, 'customeredit-button')
    CUSTOMERLIST_BUTTON = (By.ID, 'customerlist-button')
    SESSIONCREATE_BUTTON = (By.ID, 'sessioncreate-button')


class SessionFormPageLocators(object):

    DATE_FIELD = (By.NAME, 'date')
    DATEDAY_FIELD = (By.ID, 'id_date_day')
    DATEMONTH_FIELD = (By.ID, 'id_date_month')
    DATEYEAR_FIELD = (By.ID, 'id_date_year')
    TIME_FIELD = (By.NAME, 'time')
    SESSIONINVOICETYPE_FIELD = (By.NAME, 'sessionInvoiceType')
    KELAINVOICETYPE_FIELD = (By.NAME, 'kelaInvoiceType')
    SESSIONTYPE_FIELD = (By.NAME, 'sessionType')
    SESSIONDONE_FIELD = (By.NAME, 'sessionDone')
    KELAINVOICED_FIELD = (By.NAME, 'kelaInvoiced')
    CUSTOMERINVOICED_FIELD = (By.NAME, 'customerInvoiced')
    SESSIONPRICE_FIELD = (By.NAME, 'sessionprice')
    SESSIONPRICEKELAREFUND_FIELD = (By.NAME, 'sessionpriceKelaRefund')
    SESSIONSAVE_BUTTON = (By.ID, 'sessionsave-button')


class SessionDetailPageLocators(object):

    SESSIONUPDATE_LINK = (By.ID, 'sessionedit-link')
    SESSIONDELETE_LINK = (By.ID, 'sessiondelete-link')
    CUSTOMERDETAIL_LINK = (By.ID, 'customerdetail-link')

class SessionDeletePageLocators(object):

    SESSIONDELETE_BUTTON = (By.ID, 'sessiondeleteconfirmed-button')

class CompanyProfileDetailPageLocators(object):

    COMPANYPROFILEUPDATE_LINK = (By.ID, 'companyprofileupdate-link')


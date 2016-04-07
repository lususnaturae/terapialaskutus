from django.utils import timezone
from .locators import MainPageAnonymousUsersLocators, MainPageLoggedInUsersLocators, LoginPageLocators
from .locators import KelaStatementListPageLocators, KelaStatementDetailPageLocators, KelaStatementFormPageLocators
from .locators import KelaInvoiceDetailPageLocators, KelaContactProfileUpdatePageLocators


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPageAnonymousUsers(BasePage):

    def is_menu_dropdown_visible(self):
        element = self.driver.find_element(*MainPageAnonymousUsersLocators.MENU_DROPDOWN)
        return element

    def click_menu_dropdown(self):
        element = self.driver.find_element(*MainPageAnonymousUsersLocators.MENU_DROPDOWN)
        element.click()

    def is_login_navitem_visible(self):
        element = self.driver.find_element(*MainPageAnonymousUsersLocators.LOGIN_NAVITEM)
        return element

    def click_login_navitem(self):
        element = self.driver.find_element(*MainPageAnonymousUsersLocators.LOGIN_NAVITEM)
        element.click()


class MainPageLoggedInUsers(BasePage):

    def is_menu_dropdown_visible(self):
        element = self.driver.find_element(*MainPageAnonymousUsersLocators.MENU_DROPDOWN)
        return element

    def click_menu_dropdown(self):
        element = self.driver.find_element(*MainPageAnonymousUsersLocators.MENU_DROPDOWN)
        element.click()

    def is_logout_navitem_visible(self):
        element = self.driver.find_element(*MainPageLoggedInUsersLocators.LOGOUT_NAVITEM)
        return element

    def is_kelainvoicing_navitem_visible(self):
        element = self.driver.find_element(*MainPageLoggedInUsersLocators.KELAINVOICING_NAVITEM)
        return element

    def click_kelainvoicing_navitem(self):
        element = self.driver.find_element(*MainPageLoggedInUsersLocators.KELAINVOICING_NAVITEM)
        element.click()


class LoginPage(BasePage):

    def is_username_field(self):
        element = self.driver.find_element(*LoginPageLocators.USERNAME_FIELD)
        return element

    def is_password_field(self):
        element = self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
        return element

    def set_username_password(self):
        element = self.driver.find_element(*LoginPageLocators.USERNAME_FIELD)
        element.send_keys("testuser")
        element = self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
        element.send_keys("password")

    def is_signin_button(self):
        element = self.driver.find_element(*LoginPageLocators.SIGNIN_BUTTON)
        return element

    def click_signin_button(self):
        element = self.driver.find_element(*LoginPageLocators.SIGNIN_BUTTON)
        element.click()


class KelaStatementListPage(BasePage):

    def is_kelastatement_create_button_visible(self):
        element = self.driver.find_element(*KelaStatementListPageLocators.KELASTATEMENTCREATE_BUTTON)
        return element

    def click_kelastatement_create_button(self):
        element = self.driver.find_element(*KelaStatementListPageLocators.KELASTATEMENTCREATE_BUTTON)
        element.click()

    def is_kelacontactprofile_update_button_visible(self):
        element = self.driver.find_element(*KelaStatementListPageLocators.KELACONTACTPROFILEUPDATE_BUTTON)
        return element

    def click_kelacontactprofile_update_button(self):
        element = self.driver.find_element(*KelaStatementListPageLocators.KELACONTACTPROFILEUPDATE_BUTTON)
        element.click()

    #find one new Kelastatement from screen
    def is_createdkelastatement_visible(self):
        element = self.driver.find_element(*KelaStatementListPageLocators.KELASTATEMENTDETAIL_LINK)
        return element


class KelaStatementFormPage(BasePage):

    def is_date_field_visible(self):
        element = self.driver.find_element(*KelaStatementFormPageLocators.DATE_FIELD)
        return element

    def is_companyname_field_visible(self):
        element = self.driver.find_element(*KelaStatementFormPageLocators.COMPANYNAME_FIELD)
        return element

    def is_firstname_field_visible(self):
        element = self.driver.find_element(*KelaStatementFormPageLocators.FIRSTNAME_FIELD)
        return element

    def is_lastname_field_visible(self):
        element = self.driver.find_element(*KelaStatementFormPageLocators.LASTNAME_FIELD)
        return element

    def is_additionalname_field_visible(self):
        element = self.driver.find_element(*KelaStatementFormPageLocators.ADDITIONALNAME_FIELD)
        return element

    def is_ssn_field_visible(self):
        element = self.driver.find_element(*KelaStatementFormPageLocators.SSN_FIELD)
        return element

    def is_address_field_visible(self):
        element = self.driver.find_element(*KelaStatementFormPageLocators.ADDRESS_FIELD)
        return element

    def is_zipcode_field_visible(self):
        element = self.driver.find_element(*KelaStatementFormPageLocators.ZIPCODE_FIELD)
        return element

    def is_city_field_visible(self):
        element = self.driver.find_element(*KelaStatementFormPageLocators.CITY_FIELD)
        return element

    def is_telephone_field_visible(self):
        element = self.driver.find_element(*KelaStatementFormPageLocators.TELEPHONE_FIELD)
        return element

    def is_email_field_visible(self):
        element = self.driver.find_element(*KelaStatementFormPageLocators.EMAIL_FIELD)
        return element

    def is_orderno_field_visible(self):
        element = self.driver.find_element(*KelaStatementFormPageLocators.ORDERNO_FIELD)
        return element

    def is_save_button_visible(self):
        element = self.driver.find_element(*KelaStatementFormPageLocators.KELASTATEMENT_SAVE_BUTTON)
        return element

    def click_save_button(self):
        element = self.driver.find_element(*KelaStatementFormPageLocators.KELASTATEMENT_SAVE_BUTTON)
        element.click()

    def set_kelastatement_fields(self):

        fields = {
            'date': str(timezone.now().date()),
            'companyName': 'testcompanyname',
            'firstName': 'testfirstname',
            'additionalName': 'testadditionalname',
            'lastName': 'testlastname',
            'ssn': 'testssn',
            'address': 'testaddress',
            'zipCode': 'testzipcode',
            'city': 'testcity',
            'country': 'testcountry',
            'telephone': 'testtelephone',
            'email': 'testemail@example.com',
            'orderno': '100'

        }
        element = self.driver.find_element(*KelaStatementFormPageLocators.DATE_FIELD)
        element.send_keys(fields['date'])
        element = self.driver.find_element(*KelaStatementFormPageLocators.COMPANYNAME_FIELD)
        element.send_keys(fields['companyName'])

        element = self.driver.find_element(*KelaStatementFormPageLocators.FIRSTNAME_FIELD)
        element.send_keys(fields['firstName'])

        element = self.driver.find_element(*KelaStatementFormPageLocators.LASTNAME_FIELD)
        element.send_keys(fields['lastName'])

        element = self.driver.find_element(*KelaStatementFormPageLocators.ADDRESS_FIELD)
        element.send_keys(fields['address'])
        element = self.driver.find_element(*KelaStatementFormPageLocators.ZIPCODE_FIELD)
        element.send_keys(fields['zipCode'])
        element = self.driver.find_element(*KelaStatementFormPageLocators.CITY_FIELD)
        element.send_keys(fields['city'])
        element = self.driver.find_element(*KelaStatementFormPageLocators.TELEPHONE_FIELD)
        element.send_keys(fields['telephone'])
        element = self.driver.find_element(*KelaStatementFormPageLocators.EMAIL_FIELD)
        element.send_keys(fields['email'])
        element = self.driver.find_element(*KelaStatementFormPageLocators.ORDERNO_FIELD)
        element.send_keys(fields['orderno'])

    def change_customer_field_lastname(self):
        element = self.driver.find_element(*KelaStatementFormPageLocators.LASTNAME_FIELD)
        element.send_keys('changedlastname')


class KelaStatementDetailPage(BasePage):

    def is_kelastatment_list_button_visible(self):
        element = self.driver.find_element(*KelaStatementDetailPageLocators.KELASTATEMENTLIST_BUTTON)
        return element

    def click_kelastatement_list_button(self):
        element = self.driver.find_element(*KelaStatementDetailPageLocators.KELASTATEMENTLIST_BUTTON)
        element.click()


class KelaInvoiceDetailPage(BasePage):

    def is_kelastatment_list_button_visible(self):
        element = self.driver.find_element(*KelaInvoiceDetailPageLocators.KELASTATEMENTDETAIL_BUTTON)
        return element

    def click_kelastatement_list_button(self):
        element = self.driver.find_element(*KelaInvoiceDetailPageLocators.KELASTATEMENTDETAIL_BUTTON)
        element.click()


class KelaContactProfileUpdatePage(BasePage):

    def is_kelacontactprofile_save_button_visible(self):
        element = self.driver.find_element(*KelaContactProfileUpdatePageLocators.KELACONTACTPROFILE_SAVE_BUTTON)
        return element

    def click_kelacontactprofile_save_button(self):
        element = self.driver.find_element(*KelaContactProfileUpdatePageLocators.KELACONTACTPROFILE_SAVE_BUTTON)
        element.click()

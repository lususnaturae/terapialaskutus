from .locators import MainPageAnonymousUsersLocators, MainPageLoggedInUsersLocators, LoginPageLocators
from .locators import CustomerListPageLocators, CustomerFormPageLocators, CustomerDetailPageLocators
from .locators import SessionDetailPageLocators, SessionFormPageLocators, SessionDeletePageLocators
from .locators import CompanyProfileDetailPageLocators


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

    def is_customer_navitem_visible(self):
        element = self.driver.find_element(*MainPageLoggedInUsersLocators.CUSTOMER_NAVITEM)
        return element

    def click_customer_navitem(self):
        element = self.driver.find_element(*MainPageLoggedInUsersLocators.CUSTOMER_NAVITEM)
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


class CustomerListPage(BasePage):

    def is_menu_dropdown_visible(self):
        element = self.driver.find_element(*MainPageAnonymousUsersLocators.MENU_DROPDOWN)
        return element

    def click_menu_dropdown(self):
        element = self.driver.find_element(*MainPageAnonymousUsersLocators.MENU_DROPDOWN)
        element.click()

    def is_customer_navitem_visible(self):
        element = self.driver.find_element(*CustomerListPageLocators.CUSTOMER_NAVITEM)
        return element

    def is_createcustomer_navitem_visible(self):
        element = self.driver.find_element(*CustomerListPageLocators.CUSTOMER_NAVITEM)
        return element

    def click_createcustomer_link(self):
        element = self.driver.find_element(*CustomerListPageLocators.CREATECUSTOMER_LINK)
        element.click()

    def is_created_testcustomer(self, testcustomertext):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = self.driver.find_elements_by_link_text(testcustomertext)
        return element

    def click_created_testcustomer(self, testcustomertext):
        element = self.driver.find_elements_by_link_text(testcustomertext)
        element.pop().click()


    def is_testcustomer_visible(self):
        element = self.driver.find_element(*CustomerListPageLocators.TESTCUSTOMER_CARD)
        return element


class CustomerFormPage(BasePage):

    def is_firstname_field_visible(self):
        element = self.driver.find_element(*CustomerFormPageLocators.FIRSTNAME_FIELD)
        return element

    def is_lastname_field_visible(self):
        element = self.driver.find_element(*CustomerFormPageLocators.LASTNAME_FIELD)
        return element

    def is_additionalname_field_visible(self):
        element = self.driver.find_element(*CustomerFormPageLocators.ADDITIONALNAME_FIELD)
        return element

    def is_ssn_field_visible(self):
        element = self.driver.find_element(*CustomerFormPageLocators.SSN_FIELD)
        return element

    def is_address_field_visible(self):
        element = self.driver.find_element(*CustomerFormPageLocators.ADDRESS_FIELD)
        return element

    def is_zipcode_field_visible(self):
        element = self.driver.find_element(*CustomerFormPageLocators.ZIPCODE_FIELD)
        return element

    def is_city_field_visible(self):
        element = self.driver.find_element(*CustomerFormPageLocators.CITY_FIELD)
        return element

    def is_telephone_field_visible(self):
        element = self.driver.find_element(*CustomerFormPageLocators.TELEPHONE_FIELD)
        return element

    def is_email_field_visible(self):
        element = self.driver.find_element(*CustomerFormPageLocators.EMAIL_FIELD)
        return element

    def is_status_field_visible(self):
        element = self.driver.find_element(*CustomerFormPageLocators.STATUS_FIELD)
        return element

    def is_therapycategory_field_visible(self):
        element = self.driver.find_element(*CustomerFormPageLocators.THERAPYCATEGORY_FIELD)
        return element

    def is_sessionprice_field_visible(self):
        element = self.driver.find_element(*CustomerFormPageLocators.SESSIONPRICE_FIELD)
        return element

    def is_sessionpricekelarefund_field_visible(self):
        element = self.driver.find_element(*CustomerFormPageLocators.SESSIONPRICEKELAREFUND_FIELD)
        return element

    def is_statementpricekela_field_visible(self):
        element = self.driver.find_element(*CustomerFormPageLocators.STATEMENTPRICEKELA_FIELD)
        return element

    def is_save_button_visible(self):
        element = self.driver.find_element(*CustomerFormPageLocators.SAVE_BUTTON)
        return element

    def click_save_button(self):
        element = self.driver.find_element(*CustomerFormPageLocators.SAVE_BUTTON)
        element.click()

    def set_customer_fields(self):

        fields = {
            'firstName': 'testfirstname',
            'additionalName': 'testadditionalname',
            'lastName': 'testlastname',
            'ssn': 'testssn',
            'address': 'testaddress',
            'zipCode': 'testzipcode',
            'city': 'testcity',
            #'country': 'testcountry',
            'telephone': 'testtelephone',
            'email': 'testemail@example.com',
            'status': True,
            'therapyCategory': '',
            'sessionprice': 80,
            'sessionpriceKelaRefund': 52.14,
            'statementpriceKela': 22.17
        }


        element = self.driver.find_element(*CustomerFormPageLocators.FIRSTNAME_FIELD)
        element.send_keys(fields['firstName'])
        element = self.driver.find_element(*CustomerFormPageLocators.ADDITIONALNAME_FIELD)
        element.send_keys(fields['additionalName'])
        element = self.driver.find_element(*CustomerFormPageLocators.LASTNAME_FIELD)
        element.send_keys(fields['lastName'])
        element = self.driver.find_element(*CustomerFormPageLocators.SSN_FIELD)
        element.send_keys(fields['ssn'])
        element = self.driver.find_element(*CustomerFormPageLocators.ADDRESS_FIELD)
        element.send_keys(fields['address'])
        element = self.driver.find_element(*CustomerFormPageLocators.ZIPCODE_FIELD)
        element.send_keys(fields['zipCode'])
        element = self.driver.find_element(*CustomerFormPageLocators.CITY_FIELD)
        element.send_keys(fields['city'])
        element = self.driver.find_element(*CustomerFormPageLocators.TELEPHONE_FIELD)
        element.send_keys(fields['telephone'])
        element = self.driver.find_element(*CustomerFormPageLocators.EMAIL_FIELD)
        element.send_keys(fields['email'])
        element = self.driver.find_element(*CustomerFormPageLocators.SESSIONPRICE_FIELD)
        element.send_keys(fields['sessionprice'])
        element = self.driver.find_element(*CustomerFormPageLocators.SESSIONPRICEKELAREFUND_FIELD)
        element.send_keys(fields['sessionpriceKelaRefund'])
        element = self.driver.find_element(*CustomerFormPageLocators.STATEMENTPRICEKELA_FIELD)
        element.send_keys(fields['statementpriceKela'])
        # element = self.driver.find_element(*CustomerFormPageLocators.THERAPYCATEGORY_FIELD)
        # element.click()

    def change_customer_field_lastname(self):
        element = self.driver.find_element(*CustomerFormPageLocators.LASTNAME_FIELD)
        element.send_keys('changedlastname')


class CustomerDetailPage(BasePage):

    def is_customer_update_button_visible(self):
        element = self.driver.find_element(*CustomerDetailPageLocators.CUSTOMEREDIT_BUTTON)
        return element

    def click_customer_update_button(self):
        element = self.driver.find_element(*CustomerDetailPageLocators.CUSTOMEREDIT_BUTTON)
        element.click()

    def is_customer_list_button_visible(self):
        element = self.driver.find_element(*CustomerDetailPageLocators.CUSTOMERLIST_BUTTON)
        return element

    def click_customer_list_button(self):
        element = self.driver.find_element(*CustomerDetailPageLocators.CUSTOMERLIST_BUTTON)
        element.click()

    def is_session_create_button_visible(self):
        element = self.driver.find_element(*CustomerDetailPageLocators.SESSIONCREATE_BUTTON)
        return element

    def click_session_create_button(self):
        element = self.driver.find_element(*CustomerDetailPageLocators.SESSIONCREATE_BUTTON)
        element.click()

    def is_session_update_link_visible(self):
        element = self.driver.find_element_by_id("sessionupdate-link")
        return element

    def click_session_update_link(self):
        element = self.driver.find_element_by_id("sessionupdate-link")
        element.click()

    def is_one_session_date_changed(self):
        elements = self.driver.find_elements_by_link_text("31.12.2039")
        return elements


    def is_session_delete_button_visible(self):
        try:
            element = self.driver.find_element_by_id("sessiondelete-button")
        except:
            element = False

        return element

    def click_session_delete_button(self):
        element = self.driver.find_element_by_id("sessiondelete-button")
        element.click()


class SessionDetailPage(BasePage):

    def is_session_edit_link_visible(self):
        element = self.driver.find_element(*SessionDetailPageLocators.SESSIONUPDATE_LINK)
        return element

    def click_session_edit_link(self):
        element = self.driver.find_element(*SessionDetailPageLocators.SESSIONUPDATE_LINK)
        element.click()

    def is_session_delete_link_visible(self):
        element = self.driver.find_element(*SessionDetailPageLocators.SESSIONDELETE_LINK)
        return element

    def click_session_delete_link(self):
        element = self.driver.find_element(*SessionDetailPageLocators.SESSIONDELETE_LINK)
        element.click()

    def is_customer_detail_link_visible(self):
        element = self.driver.find_element(*SessionDetailPageLocators.CUSTOMERDETAIL_LINK)
        return element

    def click_customer_detail_link(self):
        element = self.driver.find_element(*SessionDetailPageLocators.CUSTOMERDETAIL_LINK)
        element.click()


class SessionFormPage(BasePage):

    def is_date_field_visible(self):
        element = self.driver.find_element(*SessionFormPageLocators.DATE_FIELD)
        return element

    def is_time_field_visible(self):
        element = self.driver.find_element(*SessionFormPageLocators.TIME_FIELD)
        return element

    def is_sessioninvoicetype_field_visible(self):
        element = self.driver.find_element(*SessionFormPageLocators.SESSIONINVOICETYPE_FIELD)
        return element

    def is_kelainvoicetype_field_visible(self):
        element = self.driver.find_element(*SessionFormPageLocators.KELAINVOICETYPE_FIELD)
        return element

    def is_sessiontype_field_visible(self):
        element = self.driver.find_element(*SessionFormPageLocators.SESSIONTYPE_FIELD)
        return element

    def is_sessiondone_field_visible(self):
        element = self.driver.find_element(*SessionFormPageLocators.SESSIONDONE_FIELD)
        return element

    def is_sessionprice_field_visible(self):
        element = self.driver.find_element(*SessionFormPageLocators.SESSIONPRICE_FIELD)
        return element

    def is_sessionpricekelarefund_field_visible(self):
        element = self.driver.find_element(*SessionFormPageLocators.SESSIONPRICEKELAREFUND_FIELD)
        return element

    def is_sessionsave_button_visible(self):
        element = self.driver.find_element(*SessionFormPageLocators.SESSIONSAVE_BUTTON)
        return element

    def click_sessionsave_button(self):
        element = self.driver.find_element(*SessionFormPageLocators.SESSIONSAVE_BUTTON)
        element.click()

    def click_customer_detail_link(self):
        element = self.driver.find_element(*SessionDetailPageLocators.CUSTOMERDETAIL_LINK)
        element.click()

    def change_date_field(self):
        # clears date fields and sets new date to 31.12.2039
        element = self.driver.find_element(*SessionFormPageLocators.DATE_FIELD)
        element.clear()
        element.send_keys("31.12.2039")


class SessionDeletePage(BasePage):

    def is_sessiondeleteconfirmation_button_visible(self):
        element = self.driver.find_element(*SessionDeletePageLocators.SESSIONDELETE_BUTTON)
        return element

    def click_sessiondeleteconfirmation_button(self):
        element = self.driver.find_element(*SessionDeletePageLocators.SESSIONDELETE_BUTTON)
        element.click()


class CompanyProfileDetailPage(BasePage):

    def is_companyprofile_update_link_visible(self):
        element = self.driver.find_element(*CompanyProfileDetailPageLocators.COMPANYPROFILEUPDATE_LINK)
        return element

    def click_companyprofile_update_link(self):
         element = self.driver.find_element(*CompanyProfileDetailPageLocators.COMPANYPROFILEUPDATE_LINK)
         element.click()


class CompanyProfileFormPage(BasePage):
    pass

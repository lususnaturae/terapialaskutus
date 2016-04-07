from .locators import MainPageAnonymousUsersLocators, MainPageLoggedInUsersLocators, LoginPageLocators
from .locators import InvoiceListPageLocators, InvoiceDetailPageLocators, GenerateInvoicePageLocators


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

    def is_customerinvoicing_navitem_visible(self):
        element = self.driver.find_element(*MainPageLoggedInUsersLocators.CUSTOMERINVOICING_NAVITEM)
        return element

    def click_customerinvoicing_navitem(self):
        element = self.driver.find_element(*MainPageLoggedInUsersLocators.CUSTOMERINVOICING_NAVITEM)
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


class InvoiceListPage(BasePage):


    def is_invoice_create_button_visible(self):
        element = self.driver.find_element(*InvoiceListPageLocators.INVOICECREATE_BUTTON)
        return element

    def is_invoice_detail_link_visible(self):
        element = self.driver.find_element(*InvoiceListPageLocators.INVOICEDETAIL_LINK)
        return element

    def click_invoice_create_button(self):
        element = self.driver.find_element(*InvoiceListPageLocators.INVOICECREATE_BUTTON)
        element.click()


class GenerateInvoicePage(BasePage):

    def is_invoice_generate_confirm_button_visible(self):
        element = self.driver.find_element(*GenerateInvoicePageLocators.CONFIRMINVOICECREATE_BUTTON)
        return element

    def click_invoice_generate_confirm_button(self):
        element = self.driver.find_element(*GenerateInvoicePageLocators.CONFIRMINVOICECREATE_BUTTON)
        element.click()

    def is_invoice_list_button_visible(self):
        element = self.driver.find_element(*GenerateInvoicePageLocators.INVOICELIST_BUTTON)
        return element

    def click_invoice_list_button(self):
        element = self.driver.find_element(*GenerateInvoicePageLocators.INVOICELIST_BUTTON)
        element.click()


class InvoiceDetailPage(BasePage):

    def is_kelastatment_list_button_visible(self):
        element = self.driver.find_element(*InvoiceDetailPageLocators.INVOICELIST_BUTTON)
        return element

    def click_kelastatement_list_button(self):
        element = self.driver.find_element(*InvoiceDetailPageLocators.INVOICELIST_BUTTON)
        element.click()



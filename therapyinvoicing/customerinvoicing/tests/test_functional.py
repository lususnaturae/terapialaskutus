from django.contrib.auth.models import Group
from django.test import LiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from ...users.tests.factories import UserFactory
from ...customers.tests.factories import SessionDoneFactory, CompanyProfileFactory
from .page import MainPageAnonymousUsers, MainPageLoggedInUsers, LoginPage
from .page import InvoiceListPage, GenerateInvoicePage


class MyLiveServerTestCase(LiveServerTestCase):

    def setUp(self):
        self.driver = WebDriver()
        self.url = self.live_server_url

    def tearDown(self):
        self.driver.quit()


class KelaStatementFunctionalTest(MyLiveServerTestCase):

    def setUp(self):
        self.driver = WebDriver()
        self.url = self.live_server_url
        user = UserFactory.create(username = "testuser", password = "password", is_active = True)
        g = Group.objects.get_or_create(name=u'therapist')
        user.groups.add(g[0].pk)
        CompanyProfileFactory.create_batch(1)
        SessionDoneFactory.create_batch(1)

    def test_user_can_login(self):

        # load the customer list page
        self.driver.get(self.url)
        mainpage = MainPageAnonymousUsers(self.driver)
        assert mainpage.is_menu_dropdown_visible(), "menu dropdown is not visible"
        mainpage.click_menu_dropdown()
        assert mainpage.is_login_navitem_visible(), "login navitem is not visible"
        mainpage.click_login_navitem()
        #login user
        login_page = LoginPage(self.driver)
        assert login_page.is_username_field(), "username field is not visible"
        assert login_page.is_password_field(), "password field is not visible"
        assert login_page.is_signin_button(), "signin button is not visible"
        login_page.set_username_password()
        login_page.click_signin_button()

    def test_can_create_invoice(self):

        self.driver.get(self.url)
        #login testuser
        mainpageanonymous = MainPageAnonymousUsers(self.driver)
        assert mainpageanonymous.is_menu_dropdown_visible(), "menu dropdown is not visible"
        mainpageanonymous.click_menu_dropdown()
        assert mainpageanonymous.is_login_navitem_visible(), "login navitem is not visible"
        mainpageanonymous.click_login_navitem()
        login_page = LoginPage(self.driver)
        assert login_page.is_username_field(), "username field is not visible"
        assert login_page.is_password_field(), "password field is not visible"
        assert login_page.is_signin_button(), "signin button is not visible"
        login_page.set_username_password()
        login_page.click_signin_button()

        mainpageloggedin = MainPageLoggedInUsers(self.driver)
        assert mainpageloggedin.is_menu_dropdown_visible(), "menu dropdown is not visible"
        mainpageloggedin.click_menu_dropdown()
        assert mainpageloggedin.is_customerinvoicing_navitem_visible(), "customerinvoicing link is not visible"
        mainpageloggedin.click_customerinvoicing_navitem()

        # invoice_list page
        invoicelist_page = InvoiceListPage(self.driver)
        assert invoicelist_page.is_invoice_create_button_visible(), "invoice create button is not visible"
        invoicelist_page.click_invoice_create_button()

        # invoice_generator_confirm page
        generateinvoice_page = GenerateInvoicePage(self.driver)
        assert generateinvoice_page.is_invoice_generate_confirm_button_visible(), "invoice generate button is not visible"
        generateinvoice_page.click_invoice_generate_confirm_button()

        # invoice_list page
        invoicelist_page = InvoiceListPage(self.driver)
        assert invoicelist_page.is_invoice_detail_link_visible(), "invoice detail link is not hidden"



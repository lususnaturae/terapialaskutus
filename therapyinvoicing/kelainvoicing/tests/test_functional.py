from django.contrib.auth.models import Group
from django.test import LiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from ...users.tests.factories import UserFactory
from ...customers.tests.factories import SessionDoneFactory, CompanyProfileFactory
from .factories import KelaContactProfileFactory
from .page import MainPageAnonymousUsers, MainPageLoggedInUsers, LoginPage
from .page import KelaStatementListPage, KelaStatementFormPage, KelaStatementDetailPage


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
        KelaContactProfileFactory.create_batch(1)
        SessionDoneFactory.create_batch(1)

    def test_user_can_login(self):
        """

        :return:
        """
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

    def test_can_create_kelastatement(self):
        """
            Test creating new customer
        :return:
        """
        self.driver.get(self.url)
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
        assert mainpageloggedin.is_kelainvoicing_navitem_visible(), "kelastatement link is not visible"
        mainpageloggedin.click_kelainvoicing_navitem()

        # kelastatement_list page
        kelastatementlist_page = KelaStatementListPage(self.driver)
        assert kelastatementlist_page.is_kelastatement_create_button_visible(), "kelastatment create button is not visible"
        kelastatementlist_page.click_kelastatement_create_button()

        # customer_form page
        kelastatementcreate_page = KelaStatementFormPage(self.driver)
        assert kelastatementcreate_page.is_date_field_visible(), "date field is not visible"
        assert kelastatementcreate_page.is_companyname_field_visible(), "companyname field is not visible"
        assert kelastatementcreate_page.is_firstname_field_visible(), "firstname field is not visible"
        assert kelastatementcreate_page.is_lastname_field_visible(), "lastname field is not visible"
        assert kelastatementcreate_page.is_address_field_visible(), "address field is not visible"
        assert kelastatementcreate_page.is_zipcode_field_visible(), "zipcode field is not visible"
        assert kelastatementcreate_page.is_city_field_visible(), "city field is not visible"
        assert kelastatementcreate_page.is_telephone_field_visible(), "telephone field is not visible"
        assert kelastatementcreate_page.is_email_field_visible(), "email field is not visible"

        assert kelastatementcreate_page.is_save_button_visible(), "save button field is not visible"
        kelastatementcreate_page.set_kelastatement_fields()
        kelastatementcreate_page.click_save_button()

        kelastatementdetail_page = KelaStatementDetailPage(self.driver)
        assert kelastatementdetail_page.is_kelastatment_list_button_visible(), "kelastatement list button is not visible"
        kelastatementdetail_page.click_kelastatement_list_button()

        # kelastatement_list page
        kelastatementlist_page = KelaStatementListPage(self.driver)
        assert kelastatementlist_page.is_kelastatement_create_button_visible(), "kelastatment create button is not visible"


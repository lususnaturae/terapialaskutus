from django.contrib.auth.models import Group
from django.test import LiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from ...users.tests.factories import UserFactory
from ...customers.tests.factories import CustomerFactory, SessionFactory
from .page import MainPageAnonymousUsers, MainPageLoggedInUsers, LoginPage
from .page import CustomerListPage, CustomerFormPage, CustomerDetailPage
from .page import SessionFormPage, SessionDeletePage


class MyLiveServerTestCase(LiveServerTestCase):

    def setUp(self):
        self.driver = WebDriver()
        self.url = self.live_server_url

    def tearDown(self):
        self.driver.quit()


class CustomerFunctionalTest(MyLiveServerTestCase):

    def setUp(self):
        self.driver = WebDriver()
        self.url = self.live_server_url
        user = UserFactory.create(username = "testuser", password = "password", is_active = True)
        g = Group.objects.get_or_create(name=u'therapist')
        user.groups.add(g[0].pk)
        CustomerFactory.create_batch(3)

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


    def test_can_create_customer(self):
        """
            Test creating new customer
        :return:
        """
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
        assert mainpageloggedin.is_customer_navitem_visible(), "customer link is not visible"
        mainpageloggedin.click_customer_navitem()

        # customer_list page
        customerlist_page = CustomerListPage(self.driver)
        assert customerlist_page.is_menu_dropdown_visible(), "menu dropdown is not visible"
        customerlist_page.click_menu_dropdown()
        assert customerlist_page.is_customer_navitem_visible(), "customer link is not visible"
        customerlist_page.click_menu_dropdown()
        assert customerlist_page.is_createcustomer_navitem_visible(), "customer create link is not visible"
        customerlist_page.click_createcustomer_link()

        # customer_form page
        customercreate_page = CustomerFormPage(self.driver)
        assert customercreate_page.is_firstname_field_visible(), "firstname field is not visible"
        assert customercreate_page.is_lastname_field_visible(), "lastname field is not visible"
        assert customercreate_page.is_additionalname_field_visible(), "additionalname field is not visible"
        assert customercreate_page.is_ssn_field_visible(), "ssn field is not visible"
        assert customercreate_page.is_address_field_visible(), "address field is not visible"
        assert customercreate_page.is_zipcode_field_visible(), "zipcode field is not visible"
        assert customercreate_page.is_city_field_visible(), "city field is not visible"
        assert customercreate_page.is_telephone_field_visible(), "telephone field is not visible"
        assert customercreate_page.is_email_field_visible(), "email field is not visible"

        assert customercreate_page.is_status_field_visible(), "status field is not visible"
        assert customercreate_page.is_sessionprice_field_visible(), "sessionprice field is not visible"
        assert customercreate_page.is_sessionpricekelarefund_field_visible(), "sessionpricekelarefund field is not visible"
        assert customercreate_page.is_save_button_visible(), "save button field is not visible"
        customercreate_page.set_customer_fields()
        customercreate_page.click_save_button()

        customerlist_page = CustomerListPage(self.driver)
        assert customerlist_page.is_testcustomer_visible(), "testcustomer card is not visible"

    def test_can_edit_customer(self):
        """
            Test editing of existing customer
            Generate 10 test customers and change lastname field by adding text changedlastname to lastname field
        :return:
        """
        testcustomers = []
        testcustomers.extend(CustomerFactory.create_batch(10))
        testcustomer = testcustomers.pop()
        testcustomersearchtext = testcustomer.lastName + ', ' + testcustomer.firstName

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
        assert mainpageloggedin.is_customer_navitem_visible(), "customer link is not visible"
        mainpageloggedin.click_customer_navitem()

        # customer_list page
        customerlist_page = CustomerListPage(self.driver)
        assert customerlist_page.is_customer_navitem_visible(), "customer link is not visible"
        assert customerlist_page.is_createcustomer_navitem_visible(), "customer create link is not visible"

        assert customerlist_page.is_created_testcustomer(testcustomersearchtext), "generated test customer is not visible"
        customerlist_page.click_created_testcustomer(testcustomersearchtext)
        customerdetail_page = CustomerDetailPage(self.driver)
        assert customerdetail_page.is_customer_update_button_visible(), "customer update button is not visible at customer_detail page"
        customerdetail_page.click_customer_update_button()

        # customer_form page
        customerform_page = CustomerFormPage(self.driver)
        assert customerform_page.is_firstname_field_visible(), "firstname field is not visible"
        assert customerform_page.is_lastname_field_visible(), "lastname field is not visible"
        assert customerform_page.is_additionalname_field_visible(), "additionalname field is not visible"
        assert customerform_page.is_ssn_field_visible(), "ssn field is not visible"
        assert customerform_page.is_address_field_visible(), "address field is not visible"
        assert customerform_page.is_zipcode_field_visible(), "zipcode field is not visible"
        assert customerform_page.is_city_field_visible(), "city field is not visible"
        assert customerform_page.is_telephone_field_visible(), "telephone field is not visible"
        assert customerform_page.is_email_field_visible(), "email field is not visible"
        assert customerform_page.is_therapycategory_field_visible(), "therapycategory field is not visible"
        assert customerform_page.is_status_field_visible(), "status field is not visible"
        assert customerform_page.is_sessionprice_field_visible(), "sessionprice field is not visible"
        assert customerform_page.is_sessionpricekelarefund_field_visible(), "sessionpricekelarefund field is not visible"
        assert customerform_page.is_save_button_visible(), "submit button field is not visible"
        customerform_page.change_customer_field_lastname()
        testcustomersearchtext = testcustomer.lastName + 'changedlastname, ' + testcustomer.firstName
        customerform_page.click_save_button()
        assert customerdetail_page.is_customer_list_button_visible(), "customer list button is not visible"
        customerdetail_page.click_customer_list_button()
        assert customerlist_page.is_created_testcustomer(testcustomersearchtext), "testcustomer card is not visible"

    def tearDown(self):
        self.driver.quit()


class SessionFunctionalTest(MyLiveServerTestCase):

    def setUp(self):
        self.driver = WebDriver()
        self.url = self.live_server_url
        user = UserFactory.create(username = "testuser", password = "password", is_active = True)
        g = Group.objects.get_or_create(name=u'therapist')
        user.groups.add(g[0].pk)
        CustomerFactory.create_batch(3)

    def test_can_create_session(self):
        testcustomers = []
        testcustomers.extend(CustomerFactory.create_batch(3))
        testcustomer = testcustomers.pop()
        testcustomersearchtext = testcustomer.lastName + ', ' + testcustomer.firstName
        testsessions = []
        testsessions.extend(SessionFactory.create_batch(3, customer=testcustomer))

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
        assert mainpageloggedin.is_customer_navitem_visible(), "customer link is not visible"
        mainpageloggedin.click_customer_navitem()

        # customer_list page
        customerlist_page = CustomerListPage(self.driver)
        assert customerlist_page.is_menu_dropdown_visible(), "menu dropdown is not visible"
        customerlist_page.click_menu_dropdown()
        assert customerlist_page.is_customer_navitem_visible(), "customer link is not visible"
        assert customerlist_page.is_createcustomer_navitem_visible(), "customer create link is not visible"
        # Open customer_detail page
        assert customerlist_page.is_created_testcustomer(testcustomersearchtext), "generated test customer is not visible"
        customerlist_page.click_created_testcustomer(testcustomersearchtext)
        customerdetail_page = CustomerDetailPage(self.driver)
        assert customerdetail_page.is_customer_update_button_visible()
        assert customerdetail_page.is_customer_list_button_visible()
        assert customerdetail_page.is_session_create_button_visible()
        customerdetail_page.click_session_create_button()

        #Create session
        sessionform_page = SessionFormPage(self.driver)
        assert sessionform_page.is_date_field_visible()
        assert sessionform_page.is_time_field_visible()

        assert sessionform_page.is_sessioninvoicetype_field_visible()
        assert sessionform_page.is_kelainvoicetype_field_visible()
        assert sessionform_page.is_sessiontype_field_visible()
        assert sessionform_page.is_sessiondone_field_visible()
        assert sessionform_page.is_sessionprice_field_visible()
        assert sessionform_page.is_sessionpricekelarefund_field_visible()
        sessionform_page.click_sessionsave_button()

        # returned to customer_detail page
        customerdetail_page.is_customer_update_button_visible()

    def test_can_update_session(self):
        testcustomers = []
        testcustomers.extend(CustomerFactory.create_batch(3))
        testcustomer = testcustomers.pop()
        testcustomersearchtext = testcustomer.lastName + ', ' + testcustomer.firstName
        testsessions = []
        testsessions.extend(SessionFactory.create_batch(10, customer=testcustomer))
        testsession = testsessions.pop()

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
        assert mainpageloggedin.is_customer_navitem_visible(), "customer link is not visible"
        mainpageloggedin.click_customer_navitem()


        # customer_list page
        customerlist_page = CustomerListPage(self.driver)
        assert customerlist_page.is_menu_dropdown_visible(), "menu dropdown is not visible"
        customerlist_page.click_menu_dropdown()
        assert customerlist_page.is_customer_navitem_visible(), "customer link is not visible"
        assert customerlist_page.is_createcustomer_navitem_visible(), "customer create link is not visible"
        # Open customer_detail page
        assert customerlist_page.is_created_testcustomer(testcustomersearchtext), "generated test customer is not visible"
        customerlist_page.click_created_testcustomer(testcustomersearchtext)
        customerdetail_page = CustomerDetailPage(self.driver)
        assert customerdetail_page.is_customer_update_button_visible()
        assert customerdetail_page.is_customer_list_button_visible()
        #assert customerdetail_page.is_one_session_date_changed()
        assert customerdetail_page.is_session_update_link_visible()
        customerdetail_page.click_session_update_link()

        sessionform_page = SessionFormPage(self.driver)
        assert sessionform_page.is_date_field_visible()
        assert sessionform_page.is_time_field_visible()

        assert sessionform_page.is_sessioninvoicetype_field_visible()
        assert sessionform_page.is_kelainvoicetype_field_visible()
        assert sessionform_page.is_sessiontype_field_visible()
        assert sessionform_page.is_sessiondone_field_visible()
        assert sessionform_page.is_sessionprice_field_visible()
        assert sessionform_page.is_sessionpricekelarefund_field_visible()
        #sessionform_page.set_session_fields()
        sessionform_page.change_date_field()
        sessionform_page.click_sessionsave_button()

        # returned to customer_detail page and check if one of sessions has new date 31.12.2039
        customerdetail_page.is_one_session_date_changed()

    def test_can_delete_session(self):
        testcustomers = []
        testcustomers.extend(CustomerFactory.create_batch(3))
        testcustomer = testcustomers.pop()
        testcustomersearchtext = testcustomer.lastName + ', ' + testcustomer.firstName
        testsessions = []
        testsessions.extend(SessionFactory.create_batch(1, customer=testcustomer))
        testsession = testsessions.pop()

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
        assert mainpageloggedin.is_customer_navitem_visible(), "customer link is not visible"
        mainpageloggedin.click_customer_navitem()

        # customer_list page
        customerlist_page = CustomerListPage(self.driver)
        assert customerlist_page.is_menu_dropdown_visible(), "menu dropdown is not visible"
        customerlist_page.click_menu_dropdown()
        assert customerlist_page.is_customer_navitem_visible(), "customer link is not visible"
        assert customerlist_page.is_createcustomer_navitem_visible(), "customer create link is not visible"
        customerlist_page.click_menu_dropdown()
        # Open customer_detail page
        assert customerlist_page.is_created_testcustomer(testcustomersearchtext), "generated test customer is not visible"
        customerlist_page.click_created_testcustomer(testcustomersearchtext)
        customerdetail_page = CustomerDetailPage(self.driver)
        assert customerdetail_page.is_customer_update_button_visible(), "customer update button is not visible"
        assert customerdetail_page.is_customer_list_button_visible(), "link to customer list is not visible"

        assert customerdetail_page.is_session_delete_button_visible(), "no sessions visible at customer detail page"
        customerdetail_page.click_session_delete_button()

        sessiondelete_page = SessionDeletePage(self.driver)
        assert sessiondelete_page.is_sessiondeleteconfirmation_button_visible(), "session delete confirmation button is not visible"
        sessiondelete_page.click_sessiondeleteconfirmation_button()

        assert not customerdetail_page.is_session_delete_button_visible(), "only session was not deleted"


class CompanyProfileFunctionalTest(MyLiveServerTestCase):
    pass

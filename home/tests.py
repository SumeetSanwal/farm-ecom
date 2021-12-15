# Create your tests here.
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase
from selenium.webdriver.chrome.webdriver import WebDriver


class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()

        # implicit wait stays in place for the entire duration that
        # the browser is open
        # poll the DOM while trying to look for an element or elements
        # for 10 seconds before throwning an exception
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):

        # quit() closes the browser
        cls.selenium.quit()

        super().tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('myuser')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('secret')
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()

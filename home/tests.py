# # Create your tests here.
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from django.test import TestCase
# from selenium.webdriver.chrome.webdriver import WebDriver


# class MySeleniumTests(StaticLiveServerTestCase):
#     fixtures = ['user-data.json']

#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.selenium = WebDriver()

#         # implicit wait stays in place for the entire duration that
#         # the browser is open
#         # poll the DOM while trying to look for an element or elements
#         # for 10 seconds before throwning an exception
#         cls.selenium.implicitly_wait(10)

#     @classmethod
#     def tearDownClass(cls):

#         # quit() closes the browser
#         cls.selenium.quit()

#         super().tearDownClass()

#     def test_login(self):
#         self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
#         username_input = self.selenium.find_element_by_name("username")
#         username_input.send_keys('myuser')
#         password_input = self.selenium.find_element_by_name("password")
#         password_input.send_keys('secret')
#         self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()


from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class Login_Test(StaticLiveServerTestCase):
    driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")

    # Create your tests here.
    driver.get("http://127.0.0.1:8000/")

    #Add new user
    driver.find_element_by_id("name").send_keys("test user")
    driver.find_element_by_id("email").send_keys("test@xyz.com")
    driver.find_element_by_id("phone").send_keys("9874561231")
    driver.find_element_by_id("pass").send_keys("test")
    driver.find_element_by_id("farmer").click()

    time.sleep(1)
    driver.find_element_by_id("signup").click()

    #login with new user
    driver.find_element_by_id("your_name").send_keys("test user")
    driver.find_element_by_id("your_pass").send_keys("test")
    driver.find_element_by_id("signin_farmer").click()
    time.sleep(1)
    driver.find_element_by_id("signin").click()

    #login user with wrong profession (Bug detected and fixed)
    driver.find_element_by_id("your_name").send_keys("test user")
    driver.find_element_by_id("your_pass").send_keys("test")
    driver.find_element_by_id("signin_customer").click()
    time.sleep(1)
    driver.find_element_by_id("signin").click()





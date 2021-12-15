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


    driver.get("http://127.0.0.1:8000/")

    #login for customer
    driver.find_element_by_id("your_name").send_keys("Pankaj")
    driver.find_element_by_id("your_pass").send_keys("pankaj")
    driver.find_element_by_id("signin_customer").click()
    time.sleep(1)
    driver.find_element_by_id("signin").click()
    time.sleep(2)

    #Add products to cart
    driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "panel-info", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "img-responsive", " " ))]').click()
    quantity = Select(driver.find_element_by_name("quantity"))  # choosing drop down box
    quantity.select_by_index(5) #changin qantity to 5
    time.sleep(2)
    driver.find_element_by_xpath('//*[(@id = "1")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-success", " " ))]').click()
    time.sleep(2)
    driver.find_element_by_link_text('Home').click()
    time.sleep(1)

    #adding more item to cart
    driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "panel-danger", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "img-responsive", " " ))]').click()
    time.sleep(1)
    quantity = Select(driver.find_element_by_name("quantity"))  # choosing drop down box
    quantity.select_by_index(3)
    time.sleep(1)
    driver.find_element_by_xpath( '//*[(@id = "10")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-success", " " ))]').click()
    time.sleep(2)

    #Removing item from cart
    driver.find_element_by_xpath('//tr[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]//a//h3').click()

    #placing order
    driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "float-right", " " ))]').click()
    time.sleep(1)
    driver.find_element_by_id("phone").send_keys("9874561231")
    driver.find_element_by_id("address").send_keys("Delhi")
    driver.find_element_by_id("pincode").send_keys("110034")
    time.sleep(2)
    driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "float-right", " " ))]').click()

    #See my orders
    driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "navbar-right", " " ))]//li[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]//a').click()

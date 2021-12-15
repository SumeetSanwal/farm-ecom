from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class Login_Test(StaticLiveServerTestCase):
    driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")


    driver.get("http://127.0.0.1:8000/")

    #login for customer
    driver.find_element_by_id("your_name").send_keys("Kishan Kumar")
    driver.find_element_by_id("your_pass").send_keys("kishan")
    driver.find_element_by_id("signin_farmer").click()
    time.sleep(1)
    driver.find_element_by_id("signin").click()
    time.sleep(2)

    #Add new product
    driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "panel-danger", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "img-responsive", " " ))]').click()
    driver.find_element_by_name('prodname').send_keys("Pumpkin")
    driver.find_element_by_name('price').send_keys("100")

    driver.find_element_by_name('image').send_keys(r"C:\Users\Sanwal\Desktop\pumpkin.jpg")
    quantity = Select(driver.find_element_by_name("cat"))  # choosing drop down box
    quantity.select_by_index(1)  # changin qantity to 5
    time.sleep(2)
    driver.find_element_by_name('submit').click()
    driver.find_element_by_link_text("Home").click()

    #View all products
    driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "panel-primary", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "img-responsive", " " ))]').click()

import pytest
from selenium import webdriver
import time
from Utilities import Baseclass
from PageObjectModel import Login
class TestadminPage(Baseclass.Baseclass):

    def test_login(self):
        logincredential = Login.LoginCredentials(self.driver)
        logincredential.Username().clear()
        time.sleep(3)
        logincredential.Username().send_keys("admin@yourstore.com")
        time.sleep(3)
        logincredential.Password().clear()
        logincredential.Password().send_keys("admin")

        logincredential.Checkbox().click()

        logincredential.Login().click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//ul[@class='sidebar-menu tree']/li[2]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/ul/li[2]/ul/li[2]/a/span").click()
        self. driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[1]/div/a").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@class='onoffswitch']/label").click()

        self.driver.find_element_by_id("Name").send_keys('chelakuty')
        self.driver.find_element_by_name("save").click()




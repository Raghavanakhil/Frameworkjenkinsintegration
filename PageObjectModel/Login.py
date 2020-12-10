from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginCredentials:

    username = (By.XPATH,"//input[@type='email']")
    password  = (By.ID,"Password")
    checkbox = (By.XPATH,"//input[@type='checkbox']")
    submit = (By.XPATH,"//input[@value='Log in']")

    def __init__(self,driver):
        self.driver = driver

    def Username(self):
        return self.driver.find_element(*LoginCredentials.username)

    def Password(self):
        return self.driver.find_element(*LoginCredentials.password)

    def Checkbox(self):
        return self.driver.find_element(*LoginCredentials.checkbox)

    def Login(self):
        return self.driver.find_element(*LoginCredentials.submit)




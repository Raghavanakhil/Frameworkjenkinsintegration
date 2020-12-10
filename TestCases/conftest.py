import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser_name",action = "store",default = "chrome")




@pytest.fixture(scope = "class")
def setUp(request):
    browser_name = request.config.getoption("browser_name")
    if(browser_name =="chrome"):
        driver = webdriver.Chrome("D:\chromedriver_win32 (1)\driver\chromedriver.exe")
        driver.get("https://admin-demo.nopcommerce.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)
        request.cls.driver = driver
        yield
        driver.close()

    elif(browser_name =="ie"):
        driver = webdriver.Ie("D:\chromedriver_win32 (1)\IEDriverServer.exe")
        driver.get("https://admin-demo.nopcommerce.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)
        request.cls.driver = driver
        yield
        driver.close()









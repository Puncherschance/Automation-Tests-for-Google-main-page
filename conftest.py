from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time


@pytest.fixture
def browser():
    print("\nStarting browser..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    link = "https://www.google.com/"
    browser.get(link)
    print("\nBegin Test Case.")
    yield browser
    print("\nQuit browser.")
    browser.quit()


##@pytest.fixture
##def enter_credentials():


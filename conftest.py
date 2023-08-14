from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from colorama import Fore, Back, Style
import time
from selenium.webdriver.chrome.options import Options #для работы с PageLoadStrategy

@pytest.fixture()
def browser():
    print(Fore.YELLOW + "\nStarting browser.")
    #options = Options()  # Задаем PageLoadStrategy
    #options.page_load_strategy = 'normal'
    #browser = webdriver.Chrome(options=options)
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.set_page_load_timeout(30)  # Устанавливаем стандартный Page_Load_Timeout для каждого теста
    #browser.implicitly_wait(5)  # Отключено, т.к. используем явные ожидания
    link = "https://www.google.com/"
    browser.get(link)
    print(Fore.YELLOW + "Begin Test Case.")
    yield browser
    time.sleep(2)
    print(Fore.YELLOW + "\nQuit browser.")
    browser.quit()


##@pytest.fixture
##def enter_credentials():


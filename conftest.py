from selenium import webdriver
import pytest
from colorama import Fore
import time
from selenium.webdriver.chrome.options import Options as OptionsChrome #для работы с Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox
# from selenium.webdriver.common.by import By
from selenium_stealth import stealth

def pytest_addoption(parser):
    parser.addoption("--language", action = "store", default = None, help = "Choose language!")
    parser.addoption("--browser_name", action = "store", default = None, help = "Choose browser for tests run!")

@pytest.fixture()
def browser(request):

    user_language = request.config.getoption("language") #  поддерживается только для Chrome
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        #chrome_options = OptionsChrome()
        print('\n', Fore.YELLOW + "\nStarting Chrome browser for tests.")
        #chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})  # не работает без использования stealth-модуля
        browser = webdriver.Chrome()#(options = chrome_options)
        stealth(browser, languages=[user_language, "es"], platform="Win32")  # As of now selenium-stealth only support Selenium Chrome.
    elif browser_name == "firefox":
        firefox_options = OptionsFirefox()
        print('\n', Fore.YELLOW + "\nStarting Firefox browser for tests.")
        firefox_options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options = firefox_options)
    else:
        raise pytest.exit("\n--browser_name should be chrome or firefox!")

    #options.page_load_strategy = 'normal'
    # browser.implicitly_wait(5)  # Отключено, т.к. используем явные ожидания
    browser.set_page_load_timeout(30)  # Устанавливаем стандартный Page_Load_Timeout для каждого теста
    browser.maximize_window()
    link = "https://www.google.com/"
    browser.get(link)
    print("Begin Test Case.")
    yield browser
    time.sleep(2)
    print("\nQuit browser.")
    browser.quit()



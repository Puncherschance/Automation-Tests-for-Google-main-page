#import time
from selenium.webdriver.common.by import By
import pytest
#from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException  # Для обработки NoSuchElementException, TimeoutException
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.chrome.options import Options  # для работы с PageLoadStrategy
#from selenium.webdriver.common.keys import Keys
from colorama import Fore


class TestGoogleMainPageSearch():  # Проверяем работоспособность поиска по тексту

    @pytest.mark.regression
    def test_search_1(self, browser):  # Поиск по тексту "Python"
        try:
            search_field = browser.find_element(By.CSS_SELECTOR, "[type = 'search']")
            search_field.send_keys("Python")
        except NoSuchElementException:
            print(Fore.RED + '\nElement is missing: search_field')
        browser.set_page_load_timeout(1)  # Необходимо обойти долгую загрузку страницы после поиска
        try:
            submit = browser.find_element(By.CSS_SELECTOR, "div.lJ9FBc > center > .gNO89b")
            submit.click()
        except TimeoutException:    # Обрабатываем TimeoutException после set_page_load_timeout
            result = browser.find_element(By.CSS_SELECTOR, "div h2 span").text
            assert result == "Python", f"Expected 'Python', got '{result}'"

    @pytest.mark.regression
    def test_search_2(self, browser):  # Поиск по тексту "Java"
        try:
            search_field = browser.find_element(By.CSS_SELECTOR, "[type = 'search']")
            search_field.send_keys("Java")
        except NoSuchElementException:
            print(Fore.RED + '\nElement is missing: search_field')
        browser.set_page_load_timeout(1)  # Необходимо обойти долгую загрузку страницы после поиска
        try:
            submit = browser.find_element(By.CSS_SELECTOR, "div.lJ9FBc > center > .gNO89b")
            submit.click()
        except TimeoutException:    # Обрабатываем TimeoutException после set_page_load_timeout
            result = browser.find_element(By.CSS_SELECTOR, "div h2 span").text
            assert result == "Java", f"Expected 'Java', got '{result}'"

    @pytest.mark.regression
    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_search_3(self, browser):  # Поиск по тексту "C++"
        try:
            search_field = browser.find_element(By.CSS_SELECTOR, "[type = 'search!']")
            search_field.send_keys("C++")
        except NoSuchElementException:
            print(Fore.RED + '\nElement is missing: search_field')
        browser.set_page_load_timeout(1)  # Необходимо обойти долгую загрузку страницы после поиска
        try:
            submit = browser.find_element(By.CSS_SELECTOR, "div.lJ9FBc > center > .gNO89b")
            submit.click()
        except TimeoutException:  # Обрабатываем TimeoutException после set_page_load_timeout
            result = browser.find_element(By.CSS_SELECTOR, "div h2 span").text
            assert result == "C++", f"Expected 'C++', got '{result}'"

class TestGoogleMainPagePictureSearch():  # Проверяем поиск по картинке

    @pytest.mark.regression
    def test_picture_search_1(self, browser):  # Делаем поиск по первой картинке
        try:
            pictures = browser.find_element(By.CSS_SELECTOR, "a[aria-label*='Поиск картинок']")
            pictures.click()
        except NoSuchElementException:
            print(Fore.RED + '\nElement is missing: pictures')
        try:
            search_field = browser.find_element(By.CSS_SELECTOR, "[type='search']")
            search_field.send_keys('Selenium')
        except NoSuchElementException:
            print(Fore.RED + '\nElement is missing: search_field')
        try:
            magnifier = browser.find_element(By.CSS_SELECTOR, ".zgAlFc span svg")
            magnifier.click()
        except NoSuchElementException:
            print(Fore.RED + '\nElement is missing: magnifier')
        try:
            image = browser.find_element(By.CSS_SELECTOR, "div a div")
            image.click()
        except NoSuchElementException:
            print(Fore.RED + '\nElement is missing: image')
        try:
            image_zoomed = browser.find_element(By.CSS_SELECTOR, "div a[role = 'link'] img[jsname='kn3ccd']")
            image_zoomed.click()
        except NoSuchElementException:
            print(Fore.RED + '\nElement is missing: image_zoomed')
        browser.switch_to.window(browser.window_handles[1])
        try:
            result = browser.find_element(By.CSS_SELECTOR, "h1.h2.lh-condensed").text
            assert result == "Selenium", f"Expected 'Selenium', got '{result}'"
        except NoSuchElementException:
            print(Fore.RED + '\nElement is missing: result')

    @pytest.mark.regression
    def test_picture_search_2(self, browser):  # Делаем поиск по второй картинке
        try:
            pictures = browser.find_element(By.CSS_SELECTOR, "a[aria-label*='Поиск картинок']")
            pictures.click()
        except NoSuchElementException:
            print(Fore.RED + '\nElement is missing: pictures')
        try:
            search_field = browser.find_element(By.CSS_SELECTOR, "[type='search']")
            search_field.send_keys('Selenium')
        except NoSuchElementException:
            print(Fore.RED + '\nElement is missing: search_field')
        try:
            magnifier = browser.find_element(By.CSS_SELECTOR, ".zgAlFc span svg")
            magnifier.click()
        except NoSuchElementException:
            print(Fore.RED + '\nElement is missing: magnifier')
        try:
            image = browser.find_element(By.CSS_SELECTOR, "div:nth-child(3) > a > div")
            image.click()
        except NoSuchElementException:
            print(Fore.RED + '\nElement is missing: image')
        try:
            image_zoomed = browser.find_element(By.CSS_SELECTOR, "div a[role = 'link'] img[jsname='kn3ccd']")
            image_zoomed.click()
        except NoSuchElementException:
            print(Fore.RED + '\nElement is missing: image_zoomed')
        browser.switch_to.window(browser.window_handles[1])
        browser.set_page_load_timeout(5)  # Необходимо обойти долгую загрузку страницы после поиска
        try:
            try:
                result = browser.find_element(By.CSS_SELECTOR, "*.infinite-scroll-container.article.last > article h1").text
                assert result == "selenium", f"Expected 'selenium', got '{result}'"
            except NoSuchElementException:
                print(Fore.RED + '\nElement is missing: result')
        except TimeoutException:  # Обрабатываем TimeoutException после set_page_load_timeout
            try:
                result = browser.find_element(By.CSS_SELECTOR, "*.infinite-scroll-container.article.last > article h1").text
                assert result == "selenium", f"Expected 'selenium', got '{result}'"
            except NoSuchElementException:
                print(Fore.RED + '\nElement is missing: result')
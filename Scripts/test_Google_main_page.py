from selenium.webdriver.common.by import By
import pytest
from selenium.common.exceptions import NoSuchElementException, TimeoutException  # Для обработки NoSuchElementException, TimeoutException
import time
#  from colorama import Fore
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#  from selenium.webdriver.chrome.options import Options  # для работы с PageLoadStrategy
#  from selenium.webdriver.common.keys import Keys


class TestSearch:  # Проверяем работоспособность поиска по тексту

    @pytest.mark.smoke
    @pytest.mark.parametrize('text', ('Python', 'Java', 'C++'))
    def test_search(self, browser, text):  # Поиск по тексту

        def result_check():
            result = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div h2 span")))
            assert result.text == text, f"\nExpected {result.text}, got {result}"

        search_field = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[type = 'search']")))
        search_field.send_keys(text)
        submit = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.lJ9FBc > center > .gNO89b")))
        submit.click()
        browser.set_page_load_timeout(2)  # Необходимо обойти долгую загрузку страницы после поиска
        try:
            result_check()
        except TimeoutException:    # Обрабатываем TimeoutException после set_page_load_timeout
            result_check()


class TestPictureSearch:  # Проверяем поиск по картинке

    @pytest.mark.smoke
    @pytest.mark.parametrize(('selector_1', 'selector_2', 'result'),
                             (('div:nth-child(2) > a > div', 'h1.h2.lh-condensed', 'Selenium'),
                              ('[alt*="Britannica"]', '*.infinite-scroll-container.article.last > article h1', 'selenium')))
    def test_picture_search(self, browser, selector_1, selector_2, result):  # Делаем поиск по картинке

        def third_site_check(): #  используем функцию для избавления от дублирующегося кода
            element = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector_2)))
            assert element.text == result, f"\nExpected {result.text}, got {element}"

        pictures = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[aria-label*='Поиск картинок']")))
        pictures.click()

        search_field = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[type='search']")))
        search_field.send_keys('Selenium')

        magnifier = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".zgAlFc span svg")))
        magnifier.click()

        image = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector_1)))
        image.click()

        image_zoomed = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div a[role = 'link'] img[jsname='kn3ccd']")))
        image_zoomed.click()

        browser.switch_to.window(browser.window_handles[1])
        browser.set_page_load_timeout(5)  # Необходимо обойти долгую загрузку страницы после поиска
        try:
            third_site_check()
        except TimeoutException:  # Обрабатываем TimeoutException после set_page_load_timeout
            third_site_check()


class TestApplicationSearch:  # Проверяем фрейм с приложениями

    @pytest.mark.smoke
    def test_application_search(self, browser):

        applications = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div a svg.gb_j")))
        applications.click()
        frame_app = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.TAG_NAME, "iframe")))
        browser.switch_to.frame(frame_app)
        app_maps = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div:nth-child(1) > ul > li:nth-child(3) div span")))
        app_maps.click()



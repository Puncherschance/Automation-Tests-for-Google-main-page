import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import pytest


class Test_Google_main_page_search():

    def test_search_1(self, browser):
        try:
            search_field = browser.find_element(By.CSS_SELECTOR, "[type = 'search']")
        except NoSuchElementException:
            print('search_field element is missing!')
        search_field.send_keys("Python")
        browser.switch_to.window(browser.window_handles[0])
        submit = browser.find_element(By.CSS_SELECTOR, "div.lJ9FBc > center > .gNO89b")
        submit.click()


    def test_search_2(self, browser):
        try:
            search_field = browser.find_element(By.CSS_SELECTOR, "[type = 'search']")
        except NoSuchElementException:
            print('search_field element is missing!')
        search_field.send_keys("Java")
        browser.switch_to.window(browser.window_handles[0])
        submit = browser.find_element(By.CSS_SELECTOR, "div.lJ9FBc > center > .gNO89b")
        submit.click()


    def test_search_3(self, browser):
        try:
            search_field = browser.find_element(By.CSS_SELECTOR, "[type = 'search']")
        except NoSuchElementException:
            print('search_field element is missing!')
        search_field.send_keys("C++")
        browser.switch_to.window(browser.window_handles[0])
        submit = browser.find_element(By.CSS_SELECTOR, "div.lJ9FBc > center > .gNO89b")
        submit.click()

class Test_Google_main_page_picture_search():

    def test_picture_search_1(self, browser):
        try:
            pictures = browser.find_element(By.CSS_SELECTOR, "a[aria-label*='Поиск картинок']")
        except NoSuchElementException:
            print('pictures element is missing')
        pictures.click()
        try:
            search_field = browser.find_element(By.CSS_SELECTOR, "[type='search']")
        except NoSuchElementException:
            print('search_field element is missing')
        search_field.send_keys('Selenium')

        try:
            magnifier = browser.find_element(By.CSS_SELECTOR, ".zgAlFc span svg path")
        except NoSuchElementException:
            print('magnifier element is missing')
        magnifier.click()
        time.sleep(3)
from pages.main_page_methods import MainPage
from pages.locators import *
import pytest
import time


class TestTextSearch:  # Поиск по тексту выводит корректный результат

    @pytest.mark.smoke
    @pytest.mark.parametrize('search_text', ('Python', 'Java', 'C++'))
    def test_search_by_text(self, browser, search_text):

        page = MainPage(browser)
        page.make_search_by_text(search_text)
        page.compare_text_search_result(search_text)


class TestImageSearch:  # Используя поиск по изображениям можно перейти на сторонний сайт

    @pytest.mark.smoke
    @pytest.mark.parametrize(("image", "locator"),
                             ((GitLocators.IMAGE_GIT, GitLocators.TEXT_GIT),
                              (BritannicaLocators.IMAGE_BRITANNICA, BritannicaLocators.TEXT_BRITANNICA)))
    def test_search_by_image(self, browser, image, locator):

        page = MainPage(browser)
        page.open_pictures_menu()
        page.make_search_by_image(text:="selenium")
        page.open_third_site(image)
        page.compare_image_search_result(locator, text)


class TestOpenApplication:  # Приложения фрейма должны корректно открываться

    @pytest.mark.smoke
    @pytest.mark.parametrize(("button_locator", "url", "text_locator", "text"),
                             ((Locators.APP_MAPS, "https://www.google.com/maps", MapsLocators.MAPS_SEARCH_FIELD, "Поиск на Google Картах"),
                              (Locators.APP_CALENDAR, "https://calendar.google.com/calendar/", CalendarLocators.CALENDAR_HEADER, "Календарь")))
    def test_application_search(self, browser, button_locator, url, text_locator, text):

        page = MainPage(browser)
        page.open_app_maps(button_locator)
        page.check_page_is_correct(url, text_locator, text)







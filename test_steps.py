from pages.main_page_methods import MainPage
from pages.locators import Locators, GitLocators, BritannicaLocators
import pytest


class TestTextSearch:  # Проверяем работоспособность поиска по тексту

    @pytest.mark.smoke
    @pytest.mark.parametrize('search_text', ('Python', 'Java', 'C++'))
    def test_search_by_text(self, browser, search_text):

        page = MainPage(browser)
        page.make_search_by_text(search_text)
        page.compare_text_search_result(search_text)


class TestImageSearch:  # Проверяем работоспособность поиска по картинке

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


class TestOpenApplication:  # Проверяем фрейм с приложениями

    @pytest.mark.smoke
    @pytest.mark.parametrize(("locator", "url"),
                             ((Locators.APP_MAPS, "https://www.google.com/maps"),
                              (Locators.APP_CALENDAR, "https://workspace.google.com/products/calendar/")))
    def test_application_search(self, browser, locator, url):

        page = MainPage(browser)
        page.open_app_maps(locator)
        page.check_page_is_correct(url)






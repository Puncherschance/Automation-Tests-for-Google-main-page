from pages.main_page_methods import MainPageMethods
from pages.locators import MainPageLocators, GitLocators, BritannicaLocators
import pytest


class TestTextSearch:  # Проверяем работоспособность поиска по тексту

    @pytest.mark.smoke
    @pytest.mark.parametrize('text', ('Python', 'Java', 'C++'))
    def test_search_by_text(self, browser, text):

        page = MainPageMethods(browser)
        page.send_text(browser, MainPageLocators.TEXT_SEARCH_FIELD, text)
        page.click_element(browser, MainPageLocators.SUBMIT_SEARCH)
        page.should_be_text(browser,MainPageLocators.TEXT_SEARCH_RESULT, text)

class TestImageSearch:  # Проверяем работоспособность поиска по картинке

    @pytest.mark.smoke
    @pytest.mark.parametrize(("image", "locator"),
                             ((GitLocators.IMAGE_GIT, GitLocators.TEXT_GIT),
                              (BritannicaLocators.IMAGE_BRITANNICA, BritannicaLocators.TEXT_BRITANNICA)))
    def test_search_by_picture(self, browser, image, locator):

        page = MainPageMethods(browser)
        page.click_element(browser, MainPageLocators.PICTURES_MENU)
        page.send_text(browser, MainPageLocators.TEXT_SEARCH_FIELD, "Selenium")
        page.click_element(browser, MainPageLocators.MAGNIFIER_ELEMENT)
        page.click_element(browser, image)
        page.click_element(browser, MainPageLocators.PICTURE_ZOOMED)
        page.switch_tab(browser)
        page.should_be_text(browser, locator, "selenium")


class TestApplicationSearch:  # Проверяем фрейм с приложениями

    @pytest.mark.smoke
    @pytest.mark.parametrize("selector", (MainPageLocators.APP_MAPS, MainPageLocators.APP_CALENDAR))
    def test_application_search(self, browser, selector):

        page = MainPageMethods(browser)
        page.click_element(browser, MainPageLocators.APPLICATIONS)
        page.select_frame_app(browser, MainPageLocators.APPLICATIONS_FRAME, selector)





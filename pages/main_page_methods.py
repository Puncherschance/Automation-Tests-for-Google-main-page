from pages.base_methods import BaseMethods
from pages.locators import Locators

class MainPage(BaseMethods):

    def make_search_by_text(self, text):
        self.send_text(Locators.TEXT_SEARCH_FIELD, text)
        self.click_element(Locators.SUBMIT_SEARCH)

    def make_search_by_image(self, text):
        self.send_text(Locators.TEXT_SEARCH_FIELD, text)
        self.click_element(Locators.MAGNIFIER_ELEMENT)

    def compare_text_search_result(self, text):
        self.should_be_text(Locators.TEXT_SEARCH_RESULT, text)

    def compare_image_search_result(self, locator, text):
        self.should_be_text(locator, text)

    def open_pictures_menu(self):
        self.click_element(Locators.PICTURES_MENU)

    def open_third_site(self, image):
        self.click_element(image)
        self.click_element(Locators.PICTURE_ZOOMED)
        self.switch_tab()

    def open_app_maps(self, locator):
        self.click_element(Locators.APPLICATIONS)
        self.select_frame_app(Locators.APPLICATIONS_FRAME, locator)

    def check_page_is_correct(self, url):
        self.compare_url(url)
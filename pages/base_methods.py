from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class BaseMethods():

    def __init__(self, browser):
        self.browser = browser

    def send_text(self, browser, element, text):
        text_search_field = WebDriverWait(browser, 5).until(EC.element_to_be_clickable(element))
        text_search_field.send_keys(text)

    def click_element(self, browser, element):
        element = WebDriverWait(browser, 5).until(EC.element_to_be_clickable(element))
        element.click()

    def should_be_text(self, browser, locator, text):

        def result_check():
            result = WebDriverWait(browser, 5).until(EC.element_to_be_clickable(locator))
            assert result.text == text, f"\nExpected {result.text}, got {result}"

        browser.set_page_load_timeout(2)
        try:
            result_check()
        except TimeoutException:
            result_check()
        except NoSuchElementException:
            return False

        return True

    def switch_tab(self, browser):
        browser.switch_to.window(browser.window_handles[1])

    def select_frame_app(self, browser, frame, selector):
        frame = WebDriverWait(browser, 5).until(EC.element_to_be_clickable(frame))
        browser.switch_to.frame(frame)

        button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable(selector))
        button.click()


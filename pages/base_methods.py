from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class BaseMethods():

    def __init__(self, browser):
        self.browser = browser

    def send_text(self, element, text):
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(element)).send_keys(text)

    def click_element(self, element):
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(element)).click()

    def should_be_text(self, locator, text):

        def assert_function():
            result = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(locator))
            assert result.text == text, f"\nExpected {text}, got {result.text}"

        self.browser.set_page_load_timeout(2)
        try:
            assert_function()
        except TimeoutException:
            assert_function()
        except NoSuchElementException:
            return False

        return True

    def switch_tab(self):
        self.browser.switch_to.window(self.browser.window_handles[1])

    def select_frame_app(self, frame, locator):
        self.browser.switch_to.frame(WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(frame)))
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(locator)).click()

    def should_be_url(self, url):
        assert url in self.browser.current_url, f"\nExpected {url} in {self.browser.current_url}"


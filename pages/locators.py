from selenium.webdriver.common.by import By

class Locators:
    TEXT_SEARCH_RESULT = (By.CSS_SELECTOR, "div h2 span")
    TEXT_SEARCH_FIELD = (By.CSS_SELECTOR, "[type = 'search']")
    SUBMIT_SEARCH = (By.CSS_SELECTOR, "div.lJ9FBc > center > .gNO89b")
    PICTURES_MENU = (By.CSS_SELECTOR, "a[aria-label*='Поиск картинок']")
    PICTURES_SEARCH_FIELD = (By.CSS_SELECTOR, "[type='search']")
    MAGNIFIER_ELEMENT = (By.CSS_SELECTOR, ".zgAlFc span svg")
    PICTURE_ZOOMED = (By.CSS_SELECTOR, "div a[role = 'link'] img[jsname='kn3ccd']")
    APPLICATIONS = (By.CSS_SELECTOR, "#gbwa div a")
    APPLICATIONS_FRAME = (By.TAG_NAME, "iframe")
    APP_MAPS = (By.CSS_SELECTOR, "div:nth-child(1) > ul > li:nth-child(3) div span")
    APP_CALENDAR = (By.CSS_SELECTOR, "div:nth-child(1) > ul > li:nth-child(12) div span")
    APP_CULTURE = (By.CSS_SELECTOR, "div:nth-child(2) > ul > li:nth-child(11) div span")
    # LOGIN_BUTTON = (By.CSS_SELECTOR, ".gb_Ad")
    # ENTER_EMAIL_FIELD = (By.CSS_SELECTOR, "[type = 'email']")
    # ENTER_PASSWORD_FIELD = (By.CSS_SELECTOR, "[type = 'password']")
    # SUBMIT_EMAIL_BUTTON = (By.CSS_SELECTOR, "#identifierNext span")
    # SUBMIT_PASSWORD_BUTTON = (By.CSS_SELECTOR, "#passwordNext > div > button > span")

class MapsLocators:
    MAPS_SEARCH_FIELD = (By.CSS_SELECTOR, "#XmI62e div label")

class CultureLocators:
    CULTURE_HEADER = (By.CSS_SELECTOR, "section:nth-child(1) div.VDJ8te span")

class CalendarLocators:
    CALENDAR_HEADER = (By.CSS_SELECTOR, ".hero-scroll__header__chapter__title")

class GitLocators:
    IMAGE_GIT = (By.CSS_SELECTOR, '[alt*=GitHub]')
    TEXT_GIT = (By.CSS_SELECTOR, 'strong a[href*="/SeleniumHQ/selenium"]')

class BritannicaLocators:
    IMAGE_BRITANNICA = (By.CSS_SELECTOR, "[alt*='Britannica']")
    TEXT_BRITANNICA = (By.CSS_SELECTOR, "*.infinite-scroll-container.article.last > article h1")

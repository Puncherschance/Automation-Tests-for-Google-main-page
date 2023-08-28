from selenium.webdriver.common.by import By

class MainPageLocators:
    TEXT_SEARCH_RESULT = (By.CSS_SELECTOR, "div h2 span")
    TEXT_SEARCH_FIELD = (By.CSS_SELECTOR, "[type = 'search']")
    SUBMIT_SEARCH = (By.CSS_SELECTOR, "div.lJ9FBc > center > .gNO89b")
    PICTURES_MENU = (By.CSS_SELECTOR, "a[aria-label*='Поиск картинок']")
    PICTURES_SEARCH_FIELD = (By.CSS_SELECTOR, "[type='search']")
    MAGNIFIER_ELEMENT = (By.CSS_SELECTOR, ".zgAlFc span svg")


    PICTURE_ZOOMED = (By.CSS_SELECTOR, "div a[role = 'link'] img[jsname='kn3ccd']")
    APPLICATIONS = (By.CSS_SELECTOR, "div a svg")
    APPLICATIONS_FRAME = (By.TAG_NAME, "iframe")
    APP_MAPS = (By.CSS_SELECTOR, "div:nth-child(1) > ul > li:nth-child(3) div span")
    APP_CALENDAR = (By.CSS_SELECTOR, "div:nth-child(1) > ul > li:nth-child(12) div span")

class GitLocators:
    IMAGE_GIT = (By.CSS_SELECTOR, '[alt*=GitHub]')
    TEXT_GIT = (By.CSS_SELECTOR, 'strong a[href*="/SeleniumHQ/selenium"]')

class BritannicaLocators:
    IMAGE_BRITANNICA = (By.CSS_SELECTOR, "[alt*='Britannica']")
    TEXT_BRITANNICA = (By.CSS_SELECTOR, "*.infinite-scroll-container.article.last > article h1")

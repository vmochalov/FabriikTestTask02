from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from settings import BASE_URL


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = BASE_URL

    def find_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(ec.visibility_of_element_located(locator))

    def find_elements(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(ec.visibility_of_all_elements_located(locator))

    def go_to_site(self, url=BASE_URL):
        return self.driver.get(url)


class Locators:
    RIGHT_SQUARE = (By.CLASS_NAME, "thechosenone")
    WRONG_SQUARE = (By.CLASS_NAME, 'missclick')
    SCORE = (By.CLASS_NAME, 'yourscore')
    PENALTY = (By.CLASS_NAME, 'yourpenalty')
    RESULT_SCREEN = (By.ID, 'resultdisplay')
    RESULT_VALUE = (By.CLASS_NAME, 'character-title')
    PLAY_AGAIN_BUTTON = (By.CLASS_NAME, 'playagain')
    BEST_RESULT_VALUE = (By.ID, 'barbest2')
    TIMER = (By.CLASS_NAME, 'clock')
    LOGO = (By.ID, 'logo')


class GamePage(BasePage):

    def click_right_square(self):
        self.find_element(Locators.RIGHT_SQUARE).click()

    def click_wrong_square(self):
        self.find_elements(Locators.WRONG_SQUARE)[0].click()

    def score_value(self):
        return int(self.find_element(Locators.SCORE).text)

    def penalty_value(self):
        return int(self.find_element(Locators.PENALTY).text)

    def result_value(self):
        return self.find_element(Locators.RESULT_VALUE).text

    def play_again(self):
        self.find_element(Locators.PLAY_AGAIN_BUTTON).click()

    def best_result(self):
        best_result_value = self.find_element(Locators.BEST_RESULT_VALUE).text
        return int(best_result_value.replace("Best result: ", ""))

    def timer_run(self):
        timer_run_value = self.find_element(Locators.TIMER).text
        return int(float(timer_run_value.replace("sec", "")))

    def find_logo(self):
        return self.find_element(Locators.LOGO)





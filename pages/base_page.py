from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout = 10)

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.wait_for_clickable(locator).click()

    def type(self, locator, text):
        self.wait_for_visible(locator).send_keys(text)

    def get_element(self, locator):
        return self.wait_for_visible(locator)

    def get_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def is_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except:
            return False

    def get_current_url(self):
        return self.driver.current_url
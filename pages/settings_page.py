from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class SettingsPage(Page):
    SETTINGS_LINK = (By.CSS_SELECTOR, "[class*= 'new-market-menu-button _1 w-inline-block']")
    SETTINGS_ITEMS = (By.CSS_SELECTOR, "[class*= 'page-setting-block w-inline-block']")
    CONNECT_COMPANY_BTN = (By.XPATH, "//div[contains(@class, 'get-free-period') and contains(text(), 'Connect the company')]")

    def go_to_settings(self):
        sleep(5)
        # self.wait_for_clickable(self.SETTINGS_LINK).click()
        #self.driver.find_element(*self.SETTINGS_LINK).click()
        #self.driver.find_element(By.CSS_SELECTOR, '.hamburger-menu-icon').click()
        wait = WebDriverWait(self.driver, 15)

        # Wait for it to be visible
        wait.until(EC.visibility_of_element_located(self.SETTINGS_LINK))

        # Then wait until clickable
        settings = wait.until(EC.element_to_be_clickable(self.SETTINGS_LINK))
        settings.click()

    def is_settings_page_open(self):
        return "/settings" in self.get_current_url()

    def count_settings_items(self):

        return len(self.get_elements(self.SETTINGS_ITEMS))

    def is_connect_company_visible(self):
        try:

            button = self.wait.until(EC.visibility_of_element_located(self.CONNECT_COMPANY_BTN))
            return button.is_displayed()
        except TimeoutException:
            print("Timeout: 'Connect the company' div is not visible.")
            return False
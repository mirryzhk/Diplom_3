from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains



class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.current_url

    def drag_and_drop(self, source, target):
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).perform()

    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)


    def open_page(self, url):
        self.driver.get(url)


    def is_element_present(self, locator, timeout=15):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_for_element(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def wait_for_element_text_to_change(self, locator, text, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: self.wait_for_element(locator).text != text
        )
        return self.wait_for_element(locator)

    def click_element(self, locator):
        self.driver.execute_script("arguments[0].click();", locator)
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    CORE UTILITY LAYER
    Provides a standardized way for all Page Objects to interact with the browser.
    This class handles synchronization (waiting) and basic element interactions.
    """
    def __init__(self,driver):
        """INITIALIZE BROWSER INSTANCE & GLOBAL WAIT TIMEOUTS"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def wait_for_element(self,locator):
        """
        SYNCHRONIZATION WRAPPER
        Ensures the UI is ready before the script attempts to interact.
        Prevents 'Flaky Tests' by waiting for visibility instead of using static sleeps.
        """
        try :
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise Exception(f"Element not visible: {locator}")

    def click(self,locator):
        """ACTIONS: ATOMIC CLICK OPERATION"""
        self.wait_for_element(locator).click()


    def send_keys(self, locator, value):
        """ACTIONS: ATOMIC TEXT INPUT OPERATION"""
        self.wait_for_element(locator).send_keys(value)




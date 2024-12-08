from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Base class for all page objects."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Common "Accept Cookies" button locator
    ACCEPT_COOKIES_BUTTON = (By.ID, "onetrust-accept-btn-handler")

    def accept_cookies(self):
        """Click the 'Accept All Cookies' button if it exists."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.ACCEPT_COOKIES_BUTTON)
            ).click()
        except Exception as e:
            print(f"Cookies banner not found or already accepted: {e}")

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        self.find_element(locator).send_keys(text)

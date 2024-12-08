from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class HomePage(BasePage):
    # Locators
    HEADER_EPAM_LOGO = (By.CSS_SELECTOR, ".header__logo-link")
    ACCEPT_COOKIES_BUTTON = (By.ID, "onetrust-accept-btn-handler")
    THEME_TOGGLE_BUTTON = (By.CSS_SELECTOR, ".theme-switcher-ui > .theme-switcher > .switch")
    LIGHT_MODE = (By.CSS_SELECTOR, ".light-mode")
    DARK_MODE = (By.CSS_SELECTOR, ".dark-mode")
    LANGUAGE_DROPDOWN = (By.CSS_SELECTOR, ".mobile-location-selector__button-section")
    #UKRAINIAN_LANGUAGE_LINK = (By.CSS_SELECTOR, '.location-selector__panel a[href="https://careers.epam.ua"]')
    UKRAINIAN_LANGUAGE_LINK = (By.CSS_SELECTOR, 'a.location-selector__link[href="https://careers.epam.ua"]')
    POLICIES_LIST = (By.CSS_SELECTOR, ".policies")
    LOCATION_TABS = (By.CSS_SELECTOR, "[role='tablist']")
    SEARCH_ICON = (By.CSS_SELECTOR, ".header-search__search-icon:nth-of-type(2)")
    SEARCH_FIELD = (By.CSS_SELECTOR, "input[placeholder='What are you looking for?']")
    SEARCH_SUBMIT = (By.CSS_SELECTOR, ".bth-text-layer")
    SEARCH_RESULTS_COUNTER = (By.CSS_SELECTOR, ".search-results__counter")

    # Methods for interactions (optional based on your needs)
    def accept_cookies(self):
        # Wait for the "Accept All" button to be clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ACCEPT_COOKIES_BUTTON)
        ).click()

    def toggle_theme(self):
        # Find all elements matching the locator
        elements = self.driver.find_elements(*self.THEME_TOGGLE_BUTTON)
        # Ensure the correct element is clicked (e.g., the second one)
        if len(elements) > 1:
            elements[1].click()  # Click the second element
        else:
            raise Exception("Expected more than one element but found fewer.")

    def switch_language_to_ua(self):
        """Switch the site's language to Ukrainian."""
        # Step 1: Locate and click the dropdown
        dropdowns = self.driver.find_elements(*self.LANGUAGE_DROPDOWN)

        if len(dropdowns) < 2:
            raise Exception("Expected at least 2 language dropdown elements, but found fewer.")

        # Click the second dropdown
        dropdowns[1].click()

        # Step 2: Wait for the Ukrainian language link to be clickable and click it
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.UKRAINIAN_LANGUAGE_LINK)
        ).click()

    def search(self, query):
        self.enter_text(self.SEARCH_FIELD, query)
        self.click_element(self.SEARCH_SUBMIT)
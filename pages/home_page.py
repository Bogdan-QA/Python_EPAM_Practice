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
    UKRAINIAN_LANGUAGE_LINK = (By.CSS_SELECTOR, 'a.location-selector__link[href="https://careers.epam.ua"]')
    POLICIES_LIST = (By.CSS_SELECTOR, ".policies")
    LOCATION_TABS = (By.CSS_SELECTOR, "[role='tablist']")
    SEARCH_ICON = (By.CSS_SELECTOR, ".header-search__search-icon")
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

    def verify_policies_list(self, expected_policies):
        """Verify the policies list contains the expected items."""
        # Get all anchor elements inside the policies list
        policies_elements = self.driver.find_elements(By.CSS_SELECTOR, f"{self.POLICIES_LIST[1]} a")

        # Extract the text from each element
        actual_policies = [policy.text.strip() for policy in policies_elements]

        # Assert that actual policies contain all the expected policies
        assert set(expected_policies).issubset(set(actual_policies)), (
            f"Expected policies not found. Expected: {expected_policies}, Found: {actual_policies}"
        )


    def verify_location_tabs(self):
        """Verify that the location tabs contain the expected regions."""
        # Locate all tabs within the LOCATION_TABS container
        tabs_elements = self.driver.find_elements(By.CSS_SELECTOR, f"{self.LOCATION_TABS[1]} a[role='tab']")

        # Extract text from each tab
        actual_tabs = [tab.text.strip() for tab in tabs_elements]

        # Expected regions
        expected_tabs = ["AMERICAS", "EMEA", "APAC"]

        # Assert that the actual tabs match the expected tabs
        assert actual_tabs == expected_tabs, (
            f"Location tabs mismatch. Expected: {expected_tabs}, Found: {actual_tabs}"
        )


    def switch_region_tab(self, region):
        """Switch to a specific region tab and verify the active state."""
        # Locate the tab for the specified region
        tabs_elements = self.driver.find_elements(By.CSS_SELECTOR, f"{self.LOCATION_TABS[1]} a[role='tab']")

        region_tab = None
        for tab in tabs_elements:
            if tab.text.strip() == region:
                region_tab = tab
                break

        if not region_tab:
            raise Exception(f"Region tab '{region}' not found!")

        # Click on the region tab
        region_tab.click()

        # Verify the clicked tab has the 'active' class
        assert "active" in region_tab.get_attribute("class"), f"Region tab '{region}' is not active!"

        # Verify other tabs do not have the 'active' class
        for tab in tabs_elements:
            if tab != region_tab:
                assert "active" not in tab.get_attribute("class"), f"Other tab '{tab.text.strip()}' is incorrectly active!"

    def search(self, query):
        # Step 1: Locate all elements matching the search icon locator
        search_icons = self.driver.find_elements(*self.SEARCH_ICON)

        if len(search_icons) < 2:
            raise Exception("Expected at least 2 search icons, but found fewer.")

        # Step 2: Click the second search icon
        search_icons[1].click()

        # Step 3: Wait for the search field to be visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SEARCH_FIELD)
        )

        # Step 4: Enter the query in the search field
        self.driver.find_element(*self.SEARCH_FIELD).send_keys(query)

        # Step 5: Submit the search query
        self.driver.find_element(*self.SEARCH_SUBMIT).click()


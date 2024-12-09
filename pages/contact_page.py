from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ContactPage(BasePage):
    # Locators
    CONTACT_US_BUTTON = (By.CSS_SELECTOR, 'a.cta-button-ui[href="https://www.epam.com/about/who-we-are/contact"]')
    REPORT_DOWNLOAD_BUTTON = (By.CSS_SELECTOR, 'a[href*="EPAM_Corporate_Overview_Q4_EOY.pdf"]')
    FORM_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button.button-ui[type="submit"]')
    FIRST_NAME_FIELD = (By.XPATH, '//div[@class="text-field-ui validation-field" and descendant::label[contains(text(),"First Name")]]')
    LAST_NAME_FIELD = (By.XPATH, '//div[@class="text-field-ui validation-field" and descendant::label[contains(text(),"Last Name")]]')
    EMAIL_FIELD = (By.XPATH, '//label[contains(text(),"Email")]/..')
    PHONE_FIELD = (By.XPATH, '//label[contains(text(),"Phone")]/..')
    HEARD_ABOUT_EPAM_FIELD = (By.XPATH, '//label[contains(text(),"How did you hear about EPAM?")]/..')
    CONSENT_CHECKBOX = (
    By.XPATH, '//input[@name="gdprConsent"]/ancestor::div[contains(@class, "checkbox__holder validation-field")]')

    def get_all_field_locators(self):
        """Return all form field locators."""
        return [
            self.FIRST_NAME_FIELD,
            self.LAST_NAME_FIELD,
            self.EMAIL_FIELD,
            self.PHONE_FIELD,
            self.HEARD_ABOUT_EPAM_FIELD,
        ]

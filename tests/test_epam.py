from conftest import home_page
from pages.home_page import HomePage
from pages.contact_page import ContactPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_epam_title(home_page):
    # Step 2: Get the page title
    actual_title = home_page.driver.title

    # Step 3: Verify the title matches the expected
    expected_title = "EPAM | Software Engineering & Product Development Services"
    assert actual_title == expected_title, f"Expected: {expected_title}, but got: {actual_title}"

def test_theme_toggle(home_page):
    # Step 1: Assert that .light-mode is not present initially
    assert len(home_page.driver.find_elements(*HomePage.LIGHT_MODE)) == 0, "Light Mode is already enabled initially!"

    # Step 2: Toggle the theme
    home_page.toggle_theme()

    # Step 3: Assert that .light-mode is now present
    assert len(home_page.driver.find_elements(*HomePage.LIGHT_MODE)) > 0, "Light Mode was not enabled after toggling!"

def test_language_switch_to_ua(home_page):
    # Step 1: Get the initial URL
    initial_url = home_page.driver.current_url

    # Step 2: Switch the language to Ukrainian
    home_page.switch_language_to_ua()

    # Step 3: Wait for the URL to change
    WebDriverWait(home_page.driver, 10).until(
        lambda driver: driver.current_url != initial_url
    )

    # Step 4: Verify the URL has changed and matches the Ukrainian site
    new_url = home_page.driver.current_url
    assert new_url != initial_url, "The URL did not change after switching language!"
    assert new_url == "https://careers.epam.ua/", f"Expected URL to be 'https://careers.epam.ua/' but got '{new_url}'"

def test_policies_list(home_page):
    # Step 1: Define the expected policies
    expected_policies = [
        "INVESTORS",
        "COOKIE POLICY",
        "OPEN SOURCE",
        "APPLICANT PRIVACY NOTICE",
        "PRIVACY POLICY",
        "WEB ACCESSIBILITY",
    ]

    # Step 2: Scroll to the bottom of the page
    home_page.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Allow time for the page to load completely

    # Step 3: Verify the policies list
    home_page.verify_policies_list(expected_policies)

def test_location_tabs(home_page):
    # Step 1: Verify the location tabs contain the expected regions
    home_page.verify_location_tabs()

    # Step 2: Switch to the "EMEA" region and verify
    home_page.switch_region_tab("EMEA")

    # Step 3: Switch to the "APAC" region and verify
    home_page.switch_region_tab("APAC")

    # Step 4: Switch back to the "AMERICAS" region and verify
    home_page.switch_region_tab("AMERICAS")


def test_search_function(home_page):
    # Step 1: Perform a search for "AI"
    home_page.search("AI")

    # Step 2: Verify the URL includes the search query
    expected_url = "https://www.epam.com/search?q=AI"
    WebDriverWait(home_page.driver, 10).until(
        EC.url_contains("search?q=AI")
    )
    assert home_page.driver.current_url == expected_url, (
        f"Expected URL: {expected_url}, but got: {home_page.driver.current_url}"
    )

    # Step 3: Verify the search results counter is visible
    assert WebDriverWait(home_page.driver, 10).until(
        EC.visibility_of_element_located(HomePage.SEARCH_RESULTS_COUNTER)
    ), "Search results counter is not visible!"


def test_form_fields_validation(custom_page):
    # Step 1: Open the desired URL and get a ContactPage object
    contact_page = custom_page("https://www.epam.com/about/who-we-are/contact")

    # Step 2: Assert that the correct page is loaded
    assert contact_page.driver.current_url == "https://www.epam.com/about/who-we-are/contact", "Failed to open the Contact page."

    # Step 3: Click the "Submit" button
    contact_page.driver.find_element(*ContactPage.FORM_SUBMIT_BUTTON).click()

    # Step 4: Validate required fields
    field_locators = contact_page.get_all_field_locators()

    for locator in field_locators:
        field_element = contact_page.driver.find_element(*locator)

        # Check the 'data-required' attribute equals "true"
        assert field_element.get_attribute('data-required') == 'true', f"Field {locator} is not marked as required."

        # Check the 'data-required-msg' attribute equals "This is a required field"
        assert field_element.get_attribute(
            'data-required-msg') == 'This is a required field', f"Incorrect required message for {locator}."

        # Check the 'validation-field' class exists on the field
        assert 'validation-field' in field_element.get_attribute(
            'class'), f"Field {locator} does not have the 'validation-field' class."

def test_company_logo_redirects_to_homepage(custom_page):
    # Step 1: Open the desired URL and get the HomePage object
    about_page = custom_page("https://www.epam.com/about")

    # Step 2: Find and click on the company logo
    logo_element = about_page.driver.find_element(*HomePage.HEADER_EPAM_LOGO)
    logo_element.click()

    # Step 3: Verify that the homepage is opened
    expected_url = "https://www.epam.com/"
    actual_url = about_page.driver.current_url
    assert actual_url == expected_url, f"Expected URL {expected_url}, but got {actual_url}."














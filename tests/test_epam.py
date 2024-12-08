from pages.home_page import HomePage
from selenium.webdriver.support.wait import WebDriverWait
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


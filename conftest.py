import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.contact_page import ContactPage

def pytest_addoption(parser):
    """Add a command-line option for selecting the browser."""
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to run tests: chrome or firefox"
    )

@pytest.fixture
def browser(request):
    """Initialize the selected browser."""
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome()  # Ensure chromedriver is in PATH
    elif browser_name == "firefox":
        driver = webdriver.Firefox()  # Ensure geckodriver is in PATH
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def home_page(browser):
    """Fixture to open EPAM website and return the HomePage object."""
    browser.get("https://www.epam.com")  # Step 1: Open the website
    home_page = HomePage(browser)  # Step 2: Create HomePage object
    try:
        home_page.accept_cookies()  # Step 3: Accept cookies if present
    except:
        pass  # Ignore errors if cookies button is not displayed
    return home_page

@pytest.fixture
def custom_page(browser):
    """Fixture to open a custom URL and return the appropriate Page object."""

    def load_page(url):
        browser.get(url)  # Open the desired URL
        if "contact" in url:
            page = ContactPage(browser)
        else:
            page = HomePage(browser)

        # Accept cookies if present
        try:
            page.accept_cookies()
        except:
            pass

        return page

    return load_page



from selenium import webdriver
from selene import config, browser
from webdriver_manager.chrome import ChromeDriverManager
import pytest

chromedriver_path = ChromeDriverManager().install()
base_url = "http://the-internet.herokuapp.com/"


@pytest.fixture(scope="session")
def setup():
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    driver.maximize_window()
    browser.set_driver(driver)
    config.timeout = 10
    yield
    browser.quit()

import pytest
from selenium.webdriver import Chrome
from homework_24.pages.autorization_page import AutorizationPage


@pytest.fixture(scope="session")
def driver() -> Chrome:
    driver = Chrome()
    driver.get("https://lms.ithillel.ua/auth")
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def autorization_page(driver):
    yield AutorizationPage(driver)

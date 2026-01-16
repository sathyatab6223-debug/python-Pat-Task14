import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def driver():
    # Setup: Initialize Chrome, maximize window, set implicit wait
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(2)
    yield driver
    driver.quit()



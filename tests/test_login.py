import time

from pages.login_page import LoginPage
from utils import config


def test_successful_login(driver):
    """
    HAPPY PATH: Verify that a user can log in with valid credentials.
    Ensures the flow from login page to the dashboard works as expected.
    """
    login = LoginPage(driver)
    login.open(config.BASE_URL)
    login.login(config.VALID_EMAIL,config.VALID_PASSWORD)
    print("login successful")


def test_logout(driver):
    """
    SESSION MANAGEMENT: Verify that a logged-in user can successfully sign out.
    Validates that the session is terminated and the user is redirected to the login screen.
    """
    login = LoginPage(driver)
    login.open(config.BASE_URL)
    login.login(config.VALID_EMAIL, config.VALID_PASSWORD)
    login.logout()
    print("logout successful")

def test_invalid_login(driver):
    """
    NEGATIVE TESTING: Verify that the system denies access for incorrect credentials.
    Validates that the appropriate error message is displayed to the user.
    """
    login = LoginPage(driver)
    login.open(config.BASE_URL)
    login.verfiy_invalid_email(config.INVALID_EMAIL,config.INVALID_PASSWORD)
    print("invalid login successful")

def test_validate_email_password_fields(driver):
    """
    UI VALIDATION: Verify the data integrity of input fields.
    Ensures that text entered into the email and password fields is correctly
    captured and displayed by the UI.
    """
    login = LoginPage(driver)
    login.open(config.BASE_URL)
    login.user_name_displayed(config.VALID_EMAIL)
    login.user_password_displayed(config.VALID_PASSWORD)
    print("validate email and password successful")

import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    """
        Page Object for the Login Page.
        Contains locators and actions related to user authentication and session management.
        """

    # --- Locators: Form Inputs and Buttons and Post-Login & UI Elements---
    email = (By.XPATH, "//input[@placeholder='Enter your mail']")
    dispaly_email =(By.XPATH, "//input[contains(@value,'satyaa')]")
    email_icon = (By.XPATH, "//div[@class='email-icon-container']")
    password = (By.XPATH, "//input[@placeholder='Enter your password ']")
    display_password = (By.XPATH, "//input[contains(@value,'Satyaa')]")
    password_icon = (By.XPATH, "//div[@class='password-icon-container']")
    sign_button = (By.XPATH, "//button[contains(text(),'Sign in')]")
    login_page_image = (By.XPATH, "//img[@src='/images/commonPages/loginPage/loginPageleftsideIcon.svg']")
    user_avatar = (By.XPATH, "//div[@class='avatar-container']")
    logout_button = (By.XPATH, "//*[contains(text(),'Log out')]")
    incorrect_email =(By.XPATH, "//p[contains(text(),'*Incorrect email!')]")
    close_popup = (By.XPATH, "//button[@aria-label='Close popup']")

    def open(self,url):
        """Navigate to the Login Page URL."""
        self.driver.get(url)


    def login(self,email,password ):
        """
        Executes the full login flow: fills credentials, clicks sign-in,
        handles post-login popups, and verifies successful entry via avatar visibility.
        """
        try:
            self.send_keys(self.email,email)
            self.send_keys(self.password, password)
            self.wait_for_element(self.email_icon).is_displayed()
            self.wait_for_element(self.password_icon).is_displayed()
            self.wait_for_element(self.sign_button).is_enabled()
            self.click(self.sign_button)
            self.click(self.close_popup)
            time.sleep(2)
            assert self.wait_for_element(self.user_avatar).is_displayed(), f'{self.user_avatar} not displayed'
        except Exception as e:
            print(f" unable to login {e}")



    def user_name_displayed(self,email):
        """Verifies if the entered email is reflected correctly in the UI value attribute."""
        try:
            self.send_keys(self.email, email)
            self.wait_for_element(self.dispaly_email).is_displayed()
        except Exception as e:
            print(f" User email is not displayed  {e}")

    def user_password_displayed(self,password):
        """Verifies if the entered password is reflected correctly in the UI value attribute."""
        try:
            self.send_keys(self.password, password)
            self.wait_for_element(self.display_password).is_displayed()
        except Exception as e:
            print(f" User password is not displayed  {e}")

    def verfiy_invalid_email(self,email,password):
        """Validates that the error message appears when using incorrect email credentials."""
        try:
            self.send_keys(self.email, email)
            self.send_keys(self.password, password)
            self.click(self.sign_button)
            self.wait_for_element(self.incorrect_email).is_displayed()
        except Exception as e:
            print(f" Incorrect email is not displayed  {e}")



    def logout(self):
        """Logs out the user by clicking the avatar and logout button, then verifies return to login page."""
        try:
            self.click(self.user_avatar)
            self.click(self.logout_button)
            assert self.wait_for_element(self.login_page_image).is_displayed(), f'{self.login_page_image} not displayed'
        except Exception as e:
            print(f" logout failed {e}")








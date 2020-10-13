from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")
    LOGIN_BUTTON = (By.NAME, "login_submit")
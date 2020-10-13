from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_item_in_basket(self):
        basket_button = self.browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        basket_button.click()
        
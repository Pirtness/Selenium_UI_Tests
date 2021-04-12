from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"

    def click_add_to_basket_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def right_product_name_in_success_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_added_to_cart_name = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_CART_NAME).text
        assert product_name == product_added_to_cart_name, f"Expected product with name {product_name} in message, got {product_added_to_cart_name}"

    def right_product_price_in_success_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_added_to_cart_price = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_CART_PRICE).text
        assert product_price == product_added_to_cart_price, f"Expected product with name {product_price} in message, got {product_added_to_cart_price}"

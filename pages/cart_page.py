from pages.base_page import BasePage

class CartPage(BasePage):

    CART_ITEMS = ".cart_item"
    REMOVE_BUTTON = "#remove-sauce-labs-backpack"
    CHECKOUT_BUTTON = "#checkout"

    def is_item_in_cart(self):
        return self.page.locator(self.CART_ITEMS).count() > 0

    def remove_item(self):
        self.click(self.REMOVE_BUTTON)

    def is_cart_empty(self):
        return self.page.locator(self.CART_ITEMS).count() == 0

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
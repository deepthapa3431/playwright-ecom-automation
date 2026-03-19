from pages.base_page import BasePage

class InventoryPage(BasePage):

    ADD_TO_CART_BACKPACK = "#add-to-cart-sauce-labs-backpack"
    CART_ICON = ".shopping_cart_link"

    def add_backpack_to_cart(self):
        self.click(self.ADD_TO_CART_BACKPACK)

    def go_to_cart(self):
        self.click(self.CART_ICON)
    
    def remove_backpack(self):
        self.click("#remove-sauce-labs-backpack")
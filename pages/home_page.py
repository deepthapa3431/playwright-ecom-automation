from pages.base_page import BasePage

class HomePage(BasePage):

    SEARCH_BOX = "#twotabsearchtextbox"
    SEARCH_BUTTON = "#nav-search-submit-button"

    def search_product(self, product_name):
        self.fill(self.SEARCH_BOX, product_name)
        self.click(self.SEARCH_BUTTON)

        self.page.wait_for_selector("div.s-main-slot")

    def get_page_title(self):
        return self.get_title()
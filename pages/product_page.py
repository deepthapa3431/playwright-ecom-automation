from pages.base_page import BasePage

class ProductPage(BasePage):

    def click_first_product(self):
        # Wait for all products to load
        products = self.page.locator("div.s-main-slot div[data-component-type='s-search-result']")
        products.first.wait_for()

        # Click the first visible product link inside it
        first_product_link = products.first.locator("h2 a")

        with self.page.context.expect_page() as new_page_info:
            first_product_link.click()

        new_page = new_page_info.value
        new_page.wait_for_load_state()

        return new_page
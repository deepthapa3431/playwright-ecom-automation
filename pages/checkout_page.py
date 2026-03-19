from pages.base_page import BasePage

class CheckoutPage(BasePage):

    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POSTAL_CODE = "#postal-code"
    CONTINUE_BUTTON = "#continue"
    FINISH_BUTTON = "#finish"
    SUCCESS_MESSAGE = ".complete-header"

    def enter_details(self, first, last, zip_code):
        self.fill(self.FIRST_NAME, first)
        self.fill(self.LAST_NAME, last)
        self.fill(self.POSTAL_CODE, zip_code)

    def continue_checkout(self):
        self.click(self.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)

    def get_success_message(self):
        return self.page.locator(self.SUCCESS_MESSAGE).text_content()
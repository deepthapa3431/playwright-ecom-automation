from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config.config import BASE_URL, USERNAME, PASSWORD

def test_checkout_flow(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    login.navigate(BASE_URL)
    login.login(USERNAME, PASSWORD)

    inventory.add_backpack_to_cart()
    inventory.go_to_cart()

    cart.click_checkout()

    checkout.enter_details("John", "Doe", "700001")
    checkout.continue_checkout()
    checkout.finish_checkout()

    assert "thank you" in checkout.get_success_message().lower()
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config.config import BASE_URL, USERNAME, PASSWORD

def test_complete_checkout_flow(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    # Login
    login.navigate(BASE_URL)
    login.login(USERNAME, PASSWORD)
    assert "inventory" in page.url.lower()

    # Add product
    inventory.add_backpack_to_cart()

    # Go to cart
    inventory.go_to_cart()
    assert cart.is_item_in_cart()

    # Remove item
    cart.remove_item()
    assert cart.is_cart_empty()

    # Add again
    page.go_back()
    inventory.add_backpack_to_cart()
    inventory.go_to_cart()

    # Checkout
    cart.click_checkout()
    checkout.enter_details("John", "Doe", "700001")
    checkout.continue_checkout()
    checkout.finish_checkout()

    # Final validation
    assert "thank you" in checkout.get_success_message().lower()
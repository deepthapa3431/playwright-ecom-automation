from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from config.config import BASE_URL, USERNAME, PASSWORD

def test_add_to_cart(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)

    login.navigate(BASE_URL)
    login.login(USERNAME, PASSWORD)

    inventory.add_backpack_to_cart()
    inventory.go_to_cart()

    assert cart.is_item_in_cart()


def test_remove_from_cart(page):
    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)

    login.navigate(BASE_URL)
    login.login(USERNAME, PASSWORD)

    inventory.add_backpack_to_cart()
    inventory.go_to_cart()

    cart.remove_item()

    assert cart.is_cart_empty()
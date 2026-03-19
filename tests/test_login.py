from pages.login_page import LoginPage
from config.config import BASE_URL, USERNAME, PASSWORD

def test_valid_login(page):
    login = LoginPage(page)

    login.navigate(BASE_URL)
    login.login(USERNAME, PASSWORD)

    assert "inventory" in page.url.lower()
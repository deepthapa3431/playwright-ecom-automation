import os
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page(request):
    with sync_playwright() as p:
        # Environment-based headless mode
        headless = os.getenv("HEADLESS", "true") == "true"

        browser = p.chromium.launch(
            headless=headless,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )

        context = browser.new_context()
        page = context.new_page()

        yield page

        context.close()
        browser.close()


# Hook for screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)

        if page:
            # Unique screenshot name (VERY IMPORTANT for parallel runs)
            test_name = item.name
            file_name = f"screenshots/{test_name}.png"

            os.makedirs("screenshots", exist_ok=True)
            page.screenshot(path=file_name)
from playwright.sync_api import Page,sync_playwright,Playwright,expect


def test_example(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page=context.new_page()
    page.goto("https://qbank.accelq.com/")
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("john.tedd")
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("john.todd")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("pass123")
    page.get_by_role("button", name="Sign In").click()
    page.pause()
    context.close()
    browser.close()
    # page.get_by_text("Log out").click()


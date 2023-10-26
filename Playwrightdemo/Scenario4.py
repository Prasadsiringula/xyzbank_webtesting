from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page.goto("https://qbank.accelq.com/")
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("john.todd")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("pass123")
    page.get_by_role("button", name="Sign In").click()
    page.get_by_text("Log out").click(button="right")
    page.get_by_text("Log out").click()

    # ---------------------

    # Stop tracing and export it into a zip archive.
    context.tracing.stop(path="trace4.zip")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

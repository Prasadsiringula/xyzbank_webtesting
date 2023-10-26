from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://qbank.accelq.com/")
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("john.todd")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("pass123")
    page.get_by_role("button", name="Sign In").click()
    page.get_by_text("Fund Transfer").click()
    page.get_by_label("Transfer from").select_option("Salary Account")
    page.get_by_label("Transfer to").select_option("Electricity Bill")
    page.get_by_label("Amount ($)").click()
    page.get_by_label("Amount ($)").fill("1")
    page.get_by_label("Memo").click()
    page.get_by_label("Memo").fill("hi")
    page.get_by_role("button", name="Submit").click()
    page.get_by_role("button", name="Go to Account Summary").click(button="right")
    page.get_by_role("button", name="Go to Account Summary").click()

    # ---------------------

    # Stop tracing and export it into a zip archive.
    context.tracing.stop(path="trace1.zip")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

from playwright.sync_api import Playwright, sync_playwright, expect


def testxyzbanklogin(setup_teardown) -> None:

    page = setup_teardown
    # page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    page.get_by_role("button", name="Customer Login").click()
   # page.wait_for_
    page.locator("#userSelect").select_option("2")
    page.get_by_role("button", name="Login").click()
    # page.get_by_role("button", name="Logout").click()
    # page.get_by_role("button", name="Home").click()

    # ---------------------







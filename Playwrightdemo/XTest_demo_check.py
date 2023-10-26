from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://cvcorp.instacks.co/dashboard")
    page.goto("https://cvcorp.instacks.co/")
    page.goto("https://cvcorp.instacks.co/login")
    page.get_by_role("textbox", name="Email").click(button="right")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("Prasadsdp000@gmail.com")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("Prasadsdp000@2001")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("button", name="Sign in").click(button="right")
    page.get_by_text("Show Password").click()

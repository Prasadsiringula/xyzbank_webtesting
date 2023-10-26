from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.google.com/")
    page.get_by_role("button", name="I'm Feeling Lucky").click()
    page.locator("#lang-chooser").select_option("en-GB")
    page.get_by_role("link", name="About").click()
    page.get_by_role("link", name="Doodles Archive").click()
    page.locator("li:nth-child(11) > .thumb-container > .thumb-image > a").click()
    page.get_by_role("link", name="Next doodle").click()
    page.get_by_role("link", name="Next doodle").click()
    page.get_by_role("link", name="Next doodle").click()
    page.get_by_text("16 Oct 2023Teacher's Day (Oct 16)").click()
    page.get_by_text("16 Oct 2023Teacher's Day (Oct 16)").click(button="right")

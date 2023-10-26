from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page.goto("https://unifiedportal-emp.epfindia.gov.in/epfo/")
    page.get_by_role("button", name="Ok").click(button="right")
    page.get_by_role("button", name="Ok").click()
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("prasad")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").click(button="right")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").click(button="right")
    page.get_by_role("textbox", name="Username").fill("G")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("BGBNG1744092000")
    page.get_by_placeholder("Enter Password").click()
    page.get_by_placeholder("Enter Password").fill("1943615")
    page.get_by_role("button", name="Sign In ").click()
    page.get_by_role("button", name="Dashboards").click()
    page.goto("https://unifiedportal-emp.epfindia.gov.in/epfo/estbReports/memberService?_HDIV_STATE_=19-42-E295B1DF152DBA4A8A69D98668EC4B95")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


@pytest.fixture()
def setup_teardown(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,executable_path=r"C:\Users\prasa\AppData\Local\Programs\Python\Python39\Lib\site-packages\playwright\driver\package\lib\server\chromium")
    context = browser.new_context()    #record_video_dir='./videos'
    page = context.new_page()
    page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    yield page
    context.close()
    browser.close()

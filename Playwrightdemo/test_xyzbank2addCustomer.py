

def testaddCustomer(setup_teardown) -> None:

    page = setup_teardown
    # page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    page.get_by_role("button", name="Bank Manager Login").click()
    page.get_by_role("button", name="Add Customer").click()
    page.get_by_placeholder("First Name").click()
    page.get_by_placeholder("First Name").click()
    page.get_by_placeholder("First Name").fill("harry")
    page.get_by_placeholder("Last Name").click()
    page.get_by_placeholder("Last Name").fill("potter")
    page.get_by_placeholder("Post Code").click()
    page.get_by_placeholder("Post Code").fill("533434")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("form").get_by_role("button", name="Add Customer").click()
    page.get_by_role("button", name="Home").click()

    # ---------------------


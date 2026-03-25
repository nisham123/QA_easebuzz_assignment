from playwright.sync_api import Page

def test_ui(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    page.click("input[value='radio1']")
    page.check("#checkBoxOption1")
    page.select_option("#dropdown-class-example", "option2")

    page.fill("#name", "Aliya")

    page.on("dialog", lambda dialog: dialog.accept())
    page.click("#alertbtn")

    assert "Practice Page" in page.title()

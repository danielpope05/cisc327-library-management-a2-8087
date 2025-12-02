from playwright.sync_api import sync_playwright

BASE_URL = "http://127.0.0.1:5000"


def test_first_flow_add_book():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(BASE_URL)

        page.click("text=Add Book")
        page.fill("input[name='title']", "Justice League")
        page.fill("input[name='author']", "Bruce Wayne")
        page.fill("input[name='isbn']", "0101010101010")
        page.fill("input[name='copies']", "4")
        page.click("text=Submit")

        page.wait_for_selector("text=Justice League")

        browser.close()


def test_sec_flow_borrow_book():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(BASE_URL)

        page.click("text=Catalog")

        row = page.locator("tr", has_text="Justice League")
        row.wait_for()

        row.locator("text=Borrow").click()
        page.fill("input[name='patron_id']", "123456")
        page.click("text=Confirm")

        html = page.content().lower()
        assert "success" in html or "borrow" in html
        
        browser.close()

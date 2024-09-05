from playwright.sync_api import sync_playwright , expect

with sync_playwright() as playwright:
    #Launch a browser
    browser = playwright.chromium.launch(headless = False, slow_mo=1000)
    #Create a page
    page = browser.new_page()
    #open a url
    page.goto("https://ultimateqa.com/automation")

    link1 = page.get_by_role("link", name="Big page with many elements")
    link1.highlight()
    link1.click()
    page.locator(".et_pb_button").first.click()
    page.locator("#et_pb_contact_name_0").click()
    page.locator("#et_pb_contact_name_0").fill("Sumit")
    page.locator("#et_pb_contact_email_0").click()
    page.locator("#et_pb_contact_email_0").fill("123@gmail.com")
    page.locator("#et_pb_contact_message_0").click()
    page.locator("#et_pb_contact_message_0").fill("test")
    page.locator("input[name=\"et_pb_contact_captcha_0\"]").click()
    page.locator("input[name=\"et_pb_contact_captcha_0\"]").fill("8")
    page.get_by_placeholder("Username").first.fill("1")
    page.get_by_placeholder("Username").first.click()
    page.get_by_placeholder("Username").first.fill("123")
    page.get_by_placeholder("Password").first.fill("12")
    page.get_by_placeholder("Password").first.click()
    page.get_by_placeholder("Password").first.fill("123")
    page.get_by_role("button", name="Login 9").first.click()
    expect(page.get_by_role("list")).to_contain_text("Error: The username 123 is not registered on this site. If you are unsure of your username, try your email address instead.")
    print.list

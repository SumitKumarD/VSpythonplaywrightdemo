from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    #Launch a browser

    browser = playwright.chromium.launch(headless=False, slow_mo=3000    )
    #maximize
    
    # Create a new page
    page = browser.new_page()
    #Launch playwright.dev
    page.goto("https://playwright.dev/python")
    #Locate Docs button and click
    docs_button = page.get_by_role('link', name= "Docs")
    docs_button.click()
    #Print url
    print("Docs_URL:" , page.url )

    #browser.close()
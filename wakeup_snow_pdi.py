from playwright.sync_api import sync_playwright # type: ignore

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(ignore_https_errors=True)

    page = context.new_page()

    page.goto("https://developer.servicenow.com/dev.do")
    with page.expect_navigation():
        page.click("button:has-text(\"Sign In\")")
    page.goto("https://signon.service-now.com/x_snc_sso_auth.do?pageId=username")
    page.locator("#email").click()
    page.locator("#email").fill("XXXXXX")
    page.get_by_role("button", name="Next").click()
    page.locator("#password").click()
    page.locator("#password").fill("XXXXX")
    with page.expect_navigation():
        page.get_by_role("button", name="Sign In").click()
    
    page.goto("https://developer.servicenow.com/dev.do")


    with page.expect_navigation():
        page.click("button:has-text(\"Start Building\")")

    page.goto("https://devxxxxx.service-now.com")


    page.screenshot(path="login.png")
    page.close()

    page.close()

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)

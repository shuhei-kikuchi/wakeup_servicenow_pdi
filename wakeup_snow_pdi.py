from playwright.sync_api import sync_playwright # type: ignore
import time
import yaml

def run(playwright):

    with open('config.yaml', 'r') as yml:
        conf = yaml.safe_load(yml)
    # conf['servicenow']['email']
    # conf['servicenow']['password']
    # conf['servicenow']['instanceurl']


    browser = playwright.chromium.launch(
        headless=True,
        args = [
            "--disable-blink-features=AutomationControlled"
            ]
        )
    
    context = browser.new_context(
        ignore_https_errors=True,
        record_video_dir="logs/", #デバッグ用に動画を取得しているが、不要ならコメント
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
        )

    page = context.new_page()
    page.goto("https://developer.servicenow.com/dev.do")
    time.sleep(3)
    with page.expect_navigation():
        page.click("button:has-text(\"Sign In\")")

    time.sleep(3)
    page.locator("#email").click()
    time.sleep(2)
    page.locator("#email").fill(conf['servicenow']['email'])
    time.sleep(2)
    page.get_by_role("button", name="Next").click()
    page.locator("#password").click()
    time.sleep(2)
    page.locator("#password").fill(conf['servicenow']['password'])
    time.sleep(2)
    with page.expect_navigation():
        page.get_by_role("button", name="Sign In").click()

    time.sleep(1)
    with page.expect_popup() as popup_info:
        page.click("button:has-text(\"Start Building\")")

    page1 = popup_info.value
    page1.goto(conf['servicenow']['instanceurl'])
    time.sleep(10) # インスタンス起動後の画面レイアウトを確認するために長めにsleep.動作確認用なので消してもOK
    page1.screenshot(path="logs/login.png")  # ログインおよびインスタンス起動後の画面の確認
    page1.close()

    page.close()

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)

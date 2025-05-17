from playwright.sync_api import sync_playwright, TimeoutError
import re

def extract_readable_text(page):
    """Try to get the most likely human-readable text from common content containers."""
    selectors_to_try = [
        "article",
        "div[itemprop='articleBody']",
        "div.story",
        "div#wrapper",
        "div#main",
        "main",
        "body"
    ]
    for selector in selectors_to_try:
        try:
            if page.locator(selector).count():
                text = page.locator(selector).inner_text()
                print(f"{selector} -------------------------------------------")
                # Clean up excessive blank lines
                return re.sub(r"\n\s*\n", "\n\n", text.strip())
        except Exception:
            continue
    return ""

def scrape_readable_text(url: str, screenshot_debug: bool = False):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        try:
            # Faster wait and more reliable on dynamic sites
            print(f"🔗 Visiting: {url}")
            page.goto(url, timeout=90000, wait_until="domcontentloaded")
            page.wait_for_timeout(3000)  # Give time for JS to load extra content

            # Try to dismiss common popups (like consent modals)
            try:
                consent_btns = page.locator("button:has-text('Accept'), button:has-text('OK')")
                if consent_btns.count():
                    consent_btns.first.click()
                    page.wait_for_timeout(1000)
            except Exception:
                pass

            if screenshot_debug:
                page.screenshot(path="debug_screenshot.png")
                print("🖼 Screenshot saved as 'debug_screenshot.png'")

            # Extract readable content
            text = extract_readable_text(page)
            return text if text.strip() else "[⚠️ No readable text found]"

        except TimeoutError as e:
            print(f"[⏱ TimeoutError] {e}")
            return "[❌ Timeout loading page]"
        except Exception as e:
            print(f"[❌ Error] {e}")
            return "[❌ General error]"
        finally:
            browser.close()

if __name__ == "__main__":
    # Test with dynamic or static websites
    # url = "https://www.w3schools.com/python/python_numbers.asp"
    url = "https://timesofindia.indiatimes.com/astrology/zodiacs-astrology/baba-vangas-chilling-prediction-comes-true-the-device-thats-becoming-a-silent-killer-for-all-ages/articleshow/121138454.cms"
    # url = "https://google.github.io/adk-docs/agents/multi-agents/"
    # url="https://google.github.io/adk-docs/callbacks/"
    # url="https://www.neuramonks.com/"
    # url="https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_setup/py_intro/py_intro.html#intro"
    # url="https://google.github.io/adk-docs/callbacks/#the-callback-mechanism-interception-and-control"

    content = scrape_readable_text(url, screenshot_debug=True)
    print("\n📄 Extracted Text Preview:\n")
    print(content[:])  # preview only first 2000 chars

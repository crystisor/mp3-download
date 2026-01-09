from playwright.sync_api import sync_playwright
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Mp3JuiceScraper:
    def __init__(self, headless=True):
        self.headless = headless
        self.base_url = "https://mp3juice.as/"

    def get_download_link(self, song_title: str) -> str:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=self.headless)
            page = browser.new_page()
            try:
                logger.info(f"Navigating to {self.base_url}")
                page.goto(self.base_url)

                # Search
                logger.info(f"Searching for: {song_title}")
                page.fill('#q', song_title)
                page.click('button[type="submit"]')

                # Wait for results and click the first download button
                # The user provided snippet: <a href="#" data-id="...">MP3 Download</a>
                # We wait for any anchor with data-id
                selector_first_dl = 'a[data-id]'
                logger.info("Waiting for search results...")
                page.wait_for_selector(selector_first_dl)
                
                # Get the first result
                # Sometimes there are multiple, we pick the first one visible
                results = page.locator(selector_first_dl)
                if results.count() == 0:
                    raise Exception("No results found.")
                
                first_result = results.first
                logger.info("Clicking first result...")
                first_result.click()

                # Wait for the second download button to appear
                # Snippet: <a href="...api/v1/download..." ...>Download</a>
                # We look for an anchor with href containing 'api/v1/download'
                selector_final_dl = 'a[href*="/api/v1/download"]'
                logger.info("Waiting for final download link...")
                page.wait_for_selector(selector_final_dl, timeout=15000) # 15s timeout

                final_button = page.locator(selector_final_dl).first
                download_url = final_button.get_attribute('href')
                
                logger.info(f"Found download URL: {download_url}")
                return download_url

            except Exception as e:
                logger.error(f"Error extracting link: {e}")
                raise e
            finally:
                browser.close()

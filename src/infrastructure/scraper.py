from playwright.sync_api import sync_playwright
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Mp3JuiceScraper:
    def __init__(self, headless=True):
        self.headless = headless
        self.base_url = "https://mp3juice.as/"

    def get_download_link(self, song_title: str) -> dict:
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

                # Wait for results
                selector_result_container = 'div.result'
                logger.info("Waiting for search results...")
                page.wait_for_selector(selector_result_container)
                
                # Get the first result container
                first_result = page.locator(selector_result_container).first
                
                # Extract the display name (e.g., "Drake - Started From the Bottom")
                # Based on user snippet: <div class="result"><div>Drake - Started From the Bottom</div>...
                display_name = first_result.locator('div').first.inner_text()
                logger.info(f"Found song: {display_name}")

                # Click the first download button inside this result
                first_result.locator('a[data-id]').first.click()

                # Wait for the final download button to appear
                selector_final_dl = 'a[href*="/api/v1/download"]'
                logger.info("Waiting for final download link...")
                page.wait_for_selector(selector_final_dl, timeout=15000)

                final_button = page.locator(selector_final_dl).first
                download_url = final_button.get_attribute('href')
                
                logger.info(f"Found download URL: {download_url}")
                return {
                    "url": download_url,
                    "display_name": display_name
                }

            except Exception as e:
                logger.error(f"Error extracting link: {e}")
                raise e
            finally:
                browser.close()

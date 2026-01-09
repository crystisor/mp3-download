from src.infrastructure.scraper import Mp3JuiceScraper
from src.infrastructure.downloader import FileDownloader
import logging

logger = logging.getLogger(__name__)

def download_song_logic(song_title: str) -> str:
    """
    Orchestrates the scraping and downloading of a song.
    """
    try:
        scraper = Mp3JuiceScraper(headless=True)
        downloader = FileDownloader(download_dir="downloads")
        
        # 1. Get the download link
        download_url = scraper.get_download_link(song_title)
        
        # 2. Download the file
        file_path = downloader.save_url_to_disk(download_url, song_title)
        
        return f"Successfully downloaded '{song_title}' to {file_path}"
        
    except Exception as e:
        logger.error(f"Error in download_song_logic: {e}")
        return f"Failed to download '{song_title}': {str(e)}"

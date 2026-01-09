from src.infrastructure.scraper import Mp3JuiceScraper
from src.infrastructure.downloader import FileDownloader
from src.infrastructure.metadata import ID3Tagger
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def download_song_logic(song_title: str) -> str:
    """
    Orchestrates the scraping and downloading of a song.
    """
    try:
        scraper = Mp3JuiceScraper(headless=True)
        downloader = FileDownloader(download_dir="downloads")
        tagger = ID3Tagger()
        
        # 1. Get the download link and song details
        song_info = scraper.get_download_link(song_title)
        download_url = song_info["url"]
        display_name = song_info["display_name"]
        
        # 2. Check if file already exists
        # Sanitize display_name for comparison
        safe_filename = "".join([c for c in display_name if c.isalpha() or c.isdigit() or c in (' ', '.', '_', '-')]).rstrip()
        if not safe_filename.lower().endswith(".mp3"):
            safe_filename += ".mp3"
        
        target_path = Path("downloads") / safe_filename
        if target_path.exists():
            logger.info(f"Skipping download: {safe_filename} already exists.")
            return f"Song already exists: {target_path.absolute()}"

        # 3. Download the file
        file_path = downloader.save_url_to_disk(download_url, display_name)
        
        # 4. Apply Metadata
        tagger.apply_metadata(file_path, display_name)
        
        return f"Successfully downloaded '{display_name}' to {file_path}"
        
    except Exception as e:
        logger.error(f"Error in download_song_logic: {e}")
        return f"Failed to download '{song_title}': {str(e)}"

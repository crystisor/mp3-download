import requests
import os
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

class FileDownloader:
    def __init__(self, download_dir: str = "downloads"):
        self.download_dir = Path(download_dir)
        self.download_dir.mkdir(parents=True, exist_ok=True)

    def save_url_to_disk(self, url: str, filename: str) -> str:
        """
        Downloads file from url and saves it as filename.
        Returns the absolute path of the saved file.
        """
        try:
            logger.info(f"Starting download: {filename}")
            response = requests.get(url, stream=True)
            response.raise_for_status()

            # Sanitize filename
            safe_filename = "".join([c for c in filename if c.isalpha() or c.isdigit() or c in (' ', '.', '_', '-')]).rstrip()
            if not safe_filename.endswith(".mp3"):
                safe_filename += ".mp3"
            
            file_path = self.download_dir / safe_filename

            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            
            logger.info(f"Download complete: {file_path}")
            return str(file_path.absolute())

        except Exception as e:
            logger.error(f"Download failed: {e}")
            raise e

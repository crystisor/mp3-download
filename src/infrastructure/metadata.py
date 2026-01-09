import logging
from pathlib import Path
from mutagen.id3 import ID3, TIT2, TPE1, ID3NoHeaderError

logger = logging.getLogger(__name__)

class ID3Tagger:
    """
    Handles writing ID3 metadata to MP3 files.
    """
    
    def apply_metadata(self, file_path: str, display_name: str):
        """
        Parses display_name (e.g., 'Artist - Title') and writes ID3 tags.
        """
        try:
            path = Path(file_path)
            if not path.exists():
                logger.error(f"File not found for tagging: {file_path}")
                return

            artist, title = self._parse_display_name(display_name)
            
            try:
                tags = ID3(file_path)
            except ID3NoHeaderError:
                tags = ID3()

            tags["TPE1"] = TPE1(encoding=3, text=artist)  # Artist
            tags["TIT2"] = TIT2(encoding=3, text=title)   # Title
            
            tags.save(file_path)
            logger.info(f"Applied ID3 tags: Artist='{artist}', Title='{title}' to {file_path}")

        except Exception as e:
            logger.error(f"Failed to apply ID3 tags: {e}")

    def _parse_display_name(self, display_name: str) -> tuple[str, str]:
        """
        Splits 'Artist - Title' into (Artist, Title).
        Defaults to Artist='Unknown' if no separator found.
        """
        if " - " in display_name:
            parts = display_name.split(" - ", 1)
            return parts[0].strip(), parts[1].strip()
        
        return "Unknown", display_name.strip()

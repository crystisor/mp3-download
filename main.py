from fastmcp import FastMCP
from src.use_cases.song_downloader import download_song_logic
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Initialize MCP Server
mcp = FastMCP("MP3 Downloader")

@mcp.tool()
def download_song(song_title: str) -> str:
    """
    Downloads an MP3 song by title from mp3juice.as.
    
    Args:
        song_title: The name of the song to download (e.g., "Bohemian Rhapsody").
        
    Returns:
        A message indicating success (with file path) or failure.
    """
    return download_song_logic(song_title)

if __name__ == "__main__":
    mcp.run()

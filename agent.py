import ollama
import json
import sys
from src.use_cases.song_downloader import download_song_logic

# Configuration
MODEL = "huihui_ai/qwen3-abliterated:8b" 

def get_user_intent(user_input: str) -> str:
    """
    Determines if the user wants to download music or just chat.
    Returns 'DOWNLOAD' or 'CHAT'.
    """
    system_prompt = """
    Analyze the user's input. 
    If the user is asking to download, save, or get specific songs/music/mp3s, return the string "DOWNLOAD".
    Otherwise (greeting, asking questions, general chat), return the string "CHAT".
    Return ONLY the word "DOWNLOAD" or "CHAT".
    """
    try:
        response = ollama.chat(model=MODEL, messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_input},
        ])
        return response['message']['content'].strip().upper()
    except:
        return "CHAT"

def get_song_list(user_prompt: str) -> list[str]:
    """
    Uses Ollama to extract a list of songs from the user's prompt.
    """
    system_prompt = """
    You are a music assistant. Your task is to extract a list of song titles from the user's input.
    Return ONLY a valid JSON array of strings. Do not add any markdown, code blocks, or extra text.
    Example: ["Song 1", "Song 2"]
    """
    
    try:
        response = ollama.chat(model=MODEL, messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt},
        ])
        
        content = response['message']['content']
        # Clean up if the model adds markdown
        content = content.strip()
        if content.startswith("```json"):
            content = content[7:]
        if content.startswith("```"):
            content = content[3:]
        if content.endswith("```"):
            content = content[:-3]
            
        songs = json.loads(content)
        if isinstance(songs, list):
            return songs
        else:
            return []
            
    except Exception as e:
        print(f"Error extracting songs: {e}")
        return []

def chat_response(user_input: str):
    """
    Standard chat response from the LLM.
    """
    try:
        stream = ollama.chat(
            model=MODEL,
            messages=[{'role': 'user', 'content': user_input}],
            stream=True,
        )
        print("\nAssistant: ", end="", flush=True)
        for chunk in stream:
            print(chunk['message']['content'], end="", flush=True)
        print("\n")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("MP3 Downloader Agent (Conversational Mode)")
    print("------------------------------------------")
    print("Type your message. Type 'exit' or 'quit' to leave.")
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
        except KeyboardInterrupt:
            break
            
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
            
        if not user_input:
            continue

        # 1. Check Intent
        intent = get_user_intent(user_input)
        
        if "DOWNLOAD" in intent:
            print(f"\n[Detected Download Request]")
            songs = get_song_list(user_input)
            
            if not songs:
                print("Could not identify specific songs to download.")
                continue
                
            print(f"Found {len(songs)} songs: {', '.join(songs)}")
            for song in songs:
                print(f"Downloading: {song}...")
                result = download_song_logic(song)
                print(f"Result: {result}")
        else:
            # 2. Normal Chat
            chat_response(user_input)

if __name__ == "__main__":
    main()

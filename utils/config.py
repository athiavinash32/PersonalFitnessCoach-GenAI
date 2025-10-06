import os
from pathlib import Path

PROMPT_DIR = Path(__file__).parent.parent

def load_system_prompt():
    """Load the system prompt from prompt.txt file."""
    try:
        filepath = PROMPT_DIR / "prompt.txt"

        if not filepath.exists():
            raise FileNotFoundError(f"prompt.txt not found in {PROMPT_DIR}")
        
        prompt_content = Path(filepath).read_text(encoding="utf-8").strip() 
        return prompt_content
    
    except FileNotFoundError as e:
        print("File not found : ",e)
        raise

    except Exception as e:
        print("Upexpected error occured while loading the system prompt : ",e)
        raise
    

def get_system_prompt():
    """Get the system prompt for the fitness coach."""
    
    return load_system_prompt()

SYSTEM_PROMPT = get_system_prompt()

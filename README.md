# PersonalFitnessCoach-GenAI

A Python-based **multi-turn personal fitness coach chatbot** powered by **Google Gemini AI**.  
This assistant provides context-aware fitness guidance, workout suggestions, and nutrition advice while maintaining conversation history.

---

## Features

- Multi-turn conversation with **context retention**.
- Uses **Google Gemini AI** for natural language understanding and response generation.
- **Customizable system prompts** for personalized coaching.
- **Retry logic** and **error handling** for API overloads (503 errors).
- Easy to extend for additional health and fitness guidance.

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/<your-username>/PersonalFitnessCoach-GenAI.git
cd PersonalFitnessCoach-GenAI
```

2. **Create and activate a virtual environment (recommended)**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
Create a .env file in the root directory:
GEMINI_API_KEY=your_google_gemini_api_key_here

5. **Usage**
Run the assistant:
```bash
python main.py
```
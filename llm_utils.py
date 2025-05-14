import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is not set")

BASE_URL = "https://api.groq.com/openai/v1/chat/completions"

def analyze_text(content: str) -> str:
    prompt = f"""You are analyzing a story to build a character interaction network.

Instructions:
1. Identify all named characters in the text.
2. Count the **total number of meaningful interactions** each character has with others.
   - Interaction means dialogue together, being in the same scene, or influencing each other’s actions.
3. For each character, list their top interaction partners and how many times they interacted.
4. Estimate counts based on context, not exact mentions.

Return the output exactly like this:

## Character Network
- **Romeo (45)**: Juliet (23), Mercutio (12), Friar (10)
- **Juliet (38)**: Romeo (23), Nurse (8), Lady Capulet (7)
- ...

Only include characters with multiple interactions. Use this structure precisely.

---

Now also extract 3–5 important direct quotes from the story. For each quote, include interaction energy label: Positive, Negative, or Neutral.

Format:

## Key Quotes
- "Quote 1..." — interaction energy: Positive
- "Quote 2..." — interactione energy: Neutral

Text:
{content}
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-70b-8192",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 1000
    }

    print("\n========== REQUEST DATA ==========")
    print(json.dumps(data, indent=2))
    print("==================================")

    try:
        response = requests.post(BASE_URL, headers=headers, json=data)
        print("\n========== RAW RESPONSE ==========")
        print(f"Status: {response.status_code}")
        print(response.text)
        print("==================================")

        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]

    except requests.exceptions.RequestException as e:
        print(f"Error calling Groq API: {e}")
        raise










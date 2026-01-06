import os
import random
from dotenv import load_dotenv

# Gemini SDK
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ---------- FALLBACK LOGIC (SAFE MODE) ----------
def _fallback_ideas(niche, audience, count):
    hooks = [
        "Top 5",
        "Beginner’s Guide to",
        "How to Start",
        "Mistakes to Avoid in",
        "Secrets of",
        "Why Most People Fail at"
    ]

    ideas = set()
    while len(ideas) < count:
        ideas.add(f"{random.choice(hooks)} {niche} for {audience}")

    return list(ideas)


# ---------- MAIN AI FUNCTION ----------
def generate_youtube_ideas(
    niche: str,
    audience: str,
    tone: str,
    count: int = 5
):
    """
    Drop-in replacement function.
    Returns: list[str]
    """

    # If API key missing → fallback
    if not GEMINI_API_KEY:
        return _fallback_ideas(niche, audience, count)

    try:
        client = genai.Client(api_key=GEMINI_API_KEY)

        # 🎯 PROMPT TUNING (THIS IS THE MAGIC)
        prompt = f"""
You are a professional YouTube growth expert.

Generate {count} UNIQUE YouTube video titles.

Niche: {niche}
Target audience: {audience}
Tone: {tone}

Rules:
- Titles must be catchy and non-repetitive
- Use emotional + curiosity hooks
- Avoid generic wording
- No numbering
- One title per line
- No explanations

Just output the titles.
"""

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        # Parse output safely
        raw_text = response.text.strip()
        ideas = [
            line.strip("•- ").strip()
            for line in raw_text.split("\n")
            if line.strip()
        ]

        # Ensure correct count
        return ideas[:count] if ideas else _fallback_ideas(niche, audience, count)

    except Exception as e:
        # If Gemini fails → fallback (VERY IMPORTANT)
        print("Gemini error:", e)
        return _fallback_ideas(niche, audience, count)

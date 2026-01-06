import re

POWER_WORDS = [
    "secret", "mistake", "truth", "fail", "top",
    "why", "how", "hidden", "viral"
]

def calculate_viral_score(title, content_type="Long Videos"):
    score = 55
    reasons = []

    title_lower = title.lower()

    # Power words (stronger impact)
    for word in POWER_WORDS:
        if word in title_lower:
            score += 8
            reasons.append(f"Power word: '{word}'")

    # Numbers = strong CTR signal
    if re.search(r"\d+", title):
        score += 12
        reasons.append("Uses numbers (CTR boost)")

    # Curiosity question
    if "?" in title:
        score += 10
        reasons.append("Curiosity-driven question")

    # Length optimization
    length = len(title)
    if content_type == "Shorts":
        if length <= 50:
            score += 12
            reasons.append("Optimized for Shorts length")
        else:
            score -= 5
    else:
        if 45 <= length <= 70:
            score += 12
            reasons.append("Ideal long-form title length")

    # Beginner targeting
    if "beginner" in title_lower:
        score += 8
        reasons.append("Beginner-friendly targeting")

    # Clamp score
    score = max(45, min(score, 95))
    return score, reasons

import random

def get_trending_topics(niche="AI", limit=5):
    pool = [
        f"{niche} tools",
        f"{niche} automation",
        f"{niche} content ideas",
        f"{niche} growth hacks",
        f"Faceless {niche} channels",
        f"{niche} shorts strategy",
        f"{niche} monetization",
        f"{niche} mistakes",
        f"{niche} beginner guide",
        f"Advanced {niche} techniques"
    ]

    random.shuffle(pool)
    return pool[:limit]

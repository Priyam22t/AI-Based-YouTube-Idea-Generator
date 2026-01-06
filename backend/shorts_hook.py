HOOKS = [
    "Stop scrolling!",
    "Nobody tells you this…",
    "This changed everything!",
    "Most people get this wrong!",
    "Watch till the end!"
]

def generate_shorts_hook(title):
    return f"{HOOKS[hash(title) % len(HOOKS)]} {title.split()[0]}…"

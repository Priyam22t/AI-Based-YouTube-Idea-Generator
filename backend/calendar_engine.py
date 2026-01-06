def generate_calendar(ideas):
    calendar = {}
    for i, idea in enumerate(ideas[:7], 1):
        calendar[f"Day {i}"] = idea
    return calendar

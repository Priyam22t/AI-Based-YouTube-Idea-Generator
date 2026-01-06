def generate_seo(title, niche):
    words = list(set(title.lower().split()))
    keywords = [w for w in words if len(w) > 3][:6]

    hashtags = [f"#{w.replace('-', '')}" for w in keywords]
    hashtags.append(f"#{niche.replace(' ', '')}")

    return keywords, hashtags

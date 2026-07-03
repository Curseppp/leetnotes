def create_slug(title: str) -> str:
    slug = "-".join(title.lower().split())
    return slug


def return_url(slug: str) -> str:
    url = f"https://leetcode.com/problems/{slug}/"
    return url

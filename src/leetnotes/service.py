


def create_url(title: str) -> str:
    slug = "-".join(title.lower().split())
    url = f"https://leetcode.com/problems/{slug}/"
    return url
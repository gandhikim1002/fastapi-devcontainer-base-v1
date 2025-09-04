base62_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def id_to_short_url(id_val: int) -> str:
    if id_val == 0:
        return base62_chars[0] 

    short_url = []
    while id_val > 0:
        remainder = id_val % 62
        short_url.append(base62_chars[remainder])
        id_val //= 62
    return "".join(reversed(short_url))


def short_url_to_id(short_url: str) -> int:
    id_val = 0
    for char in short_url:
        id_val = id_val * 62 + base62_chars.index(char) 

    return id_val

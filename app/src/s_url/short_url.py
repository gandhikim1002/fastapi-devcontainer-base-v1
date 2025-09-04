class URLShortener:
    def __init__(self):
        self.base62_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.char_to_int = {char: i for i, char in enumerate(self.base62_chars)}

    def id_to_short_url(self, id_val: int) -> str:
        """Converts an integer ID to a base-62 short URL string."""
        if id_val == 0:
            return self.base62_chars[0]  # Handle ID 0 specifically

        short_url = []
        while id_val > 0:
            remainder = id_val % 62
            short_url.append(self.base62_chars[remainder])
            id_val //= 62
        return "".join(reversed(short_url))

    def short_url_to_id(self, short_url: str) -> int:
        """Converts a base-62 short URL string back to an integer ID."""
        id_val = 0
        for char in short_url:
            id_val = id_val * 62 + self.char_to_int[char]
        return id_val

'''
# Example Usage:
shortener = URLShortener()

original_id = 123456789
short_code = shortener.id_to_short_url(original_id)
print(f"Original ID: {original_id}, Short Code: {short_code}")

retrieved_id = shortener.short_url_to_id(short_code)
print(f"Short Code: {short_code}, Retrieved ID: {retrieved_id}")
'''
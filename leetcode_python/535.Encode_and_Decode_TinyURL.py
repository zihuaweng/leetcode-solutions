# https://leetcode.com/problems/encode-and-decode-tinyurl/

class Codec:
    
    def __init__(self):
        self.short2long = {}
        self.long2short = {}
        self.string = string.ascii_letters + '1234567890'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while longUrl not in self.long2short:    # equals to a do while loop
            url = ''
            for _ in range(7):
                url += self.string[random.randint(0, 61)]
            if url in self.short2long:
                continue
            self.short2long[url] = longUrl
            self.long2short[longUrl] = url
        return url
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.short2long[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
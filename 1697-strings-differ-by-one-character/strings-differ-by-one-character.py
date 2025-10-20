class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        seen = set()
        for word in dict:
            for i in range(len(word)):
                masked = hash(word[:i] + "*" + word[i+1:])
                if masked in seen:
                    return True
                seen.add(masked)
        return False
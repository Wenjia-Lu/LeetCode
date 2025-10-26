class Solution:
    def canTransform(self, s1, s2):
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1 
            if count > 1:
                # print(f"cant transform {s1}, {s2}")
                return False
        # print(f"can transform {s1}, {s2}")
        return True
    
    def gen(self, s):
        combo = set()
        tmp = list(s)
        for i in range(len(s)):
            for z in range(26):
                tmp[i] = chr(ord('a') + z)
                combo.add("".join(tmp))
            tmp[i] = s[i]
        combo.remove(s)
        return combo

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words or beginWord == endWord:
            return 0
        q = collections.deque([(beginWord, 1)])
        width = 1
        seen = set()
        seen.add(beginWord)

        while q:
            k = width
            # print(f"loop {k} times: ")
            width = 0
            curr, layer = q.popleft()
            # print(f"layer {layer}: {curr}")
            combo = self.gen(curr)
            for word in combo:
                if word not in words: continue
                if word in seen: continue
                if self.canTransform(curr, word):
                    if word == endWord:
                        return layer + 1
                    seen.add(word)
                    q.append((word, layer + 1))
                    # print("added ", word)
                    width += 1
        return 0


        

        
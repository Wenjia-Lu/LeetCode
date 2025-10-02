class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            key = "".join(sorted(s))
            val = d.get(key, [])
            val.append(s)
            d[key] = val
        return list(d.values())
        
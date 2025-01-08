class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            a = ''.join(sorted(s))
            if a in d:
                d[a].append(s) 
            else:
                d[a] = [s]
        
        return list(d.values())

        
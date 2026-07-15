class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        all_anagrams = []

        for s in strs:
            tmp = frozenset(s)
            if tmp in hm:
                hm[tmp].append(s)
            else:
                hm[tmp] = [s]
        
        for key, value in enumerate(hm):
            all_anagrams.append(hm[value])

        return all_anagrams
# https://leetcode.com/problems/valid-anagram/description/

# Bruteforce Approach
# Approach: Use hash tables to count occurances of a character in the string. Tally them to see if it's an anagram.
# Time complexity: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tmps = {}
        tmpt = {}

        for l in s:
            if l not in tmps:
                tmps[l] = 1
                continue
            tmps[l] = tmps[l] + 1

        for c in t:
            if c not in tmpt:
                tmpt[c] = 1
                continue
            tmpt[c] = tmpt[c] + 1

        if set(s) == set(t) and len(tmps) == len(tmpt):
            for key in tmps:
                if tmps[key] != tmpt[key]:
                    return False
            return True

        return False
# https://leetcode.com/problems/contains-duplicate/

# Bruteforce Approach
# Time Complexity: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checked = {}
        for n in nums:
            if n not in checked.keys():
                checked[n] = 1
            else:
                checked[n] = checked[n] + 1
            
            if checked[n] > 1:
                return True

        return False

# Optimzed Approach
# Time Complexity: O(n)
# Con: It cannot "early-exit." Even if the very first two numbers in a million-item list are duplicates, 
# this code will still process the entire list and build the entire set before giving you an answer.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums))!=len(nums)
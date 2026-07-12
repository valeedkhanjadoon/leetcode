# https://leetcode.com/problems/two-sum/description/

# Bruteforce Approach
# Time Complexity: O(n^2)
# Using two for loops to find the sum of two numbers in the list
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]

# Optimized Approach
# Time Complexity: O(n)
# Using Hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in record:
                return [i, record[difference]]
            record[nums[i]] = i
            
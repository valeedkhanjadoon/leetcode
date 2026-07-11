# https://leetcode.com/problems/valid-parentheses/description/

# Bruteforce Approach
#Time Complexity: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            elif len(stack) > 0 and stack[-1] == "(" and char == ")":
                stack.pop()
            elif len(stack) > 0 and stack[-1] == "[" and char == "]":
                stack.pop()
            elif len(stack) > 0 and stack[-1] == "{" and char == "}":
                stack.pop()
            else:
                return False

        if stack == []:
            return True
        else:
            return False

'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

'''
PARENTHESES = {
    "{": "}",
    "(": ")",
    "[": "]"
}


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for char in s:
            if char in PARENTHESES.keys():
                stack.append(char)
            else:
                if len(stack) == 0 or PARENTHESES[stack.pop()] != char:
                    return False
        
        return len(stack) == 0

### ------------ DELETE THESE BLOCKS(62-68) WHEN SEND TO LEET CODE ------------ ###

if __name__ == "__main__":
    s = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    for val in s:
        result = Solution().isValid(val)
        print(result)
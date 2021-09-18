'''
Given the head of a singly linked list, return true if it is a palindrome.
Input: head = [1,2,2,1]
Output: true
'''
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    @classmethod
    def isPalindrome(self, head: ListNode):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp = head
        stack = []
        length_of_stack = 0
        is_palin = True

        while temp:
            stack.append(temp.val)
            length_of_stack += 1
            temp = temp.next

        for _ in range(length_of_stack // 2):
            poped_stack = stack.pop()

            if head.val != poped_stack:
                is_palin = False
                break
            
            head = head.next

        stack = None
        return is_palin


### ------------ DELETE THESE BLOCKS(42-55) WHEN SEND TO LEET CODE ------------ ###
if __name__ == "__main__":
    p7 = ListNode(1)
    p6 = ListNode(1,p7)
    p5 = ListNode(2,p6)
    p4 = ListNode(3,p5)
    p3 = ListNode(3,p4)
    p2 = ListNode(2,p3)
    p1 = ListNode(1,p2)

    res = Solution.isPalindrome(p1)
    
    print(res)

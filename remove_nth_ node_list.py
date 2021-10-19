'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def init(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return 
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        if length == 1 and n == 1:
            return
        elif length == n:
            head = head.next
            return head

        temp = head
        for _ in range(1, length - n):
            temp = temp.next

        temp.next = temp.next.next
        return head
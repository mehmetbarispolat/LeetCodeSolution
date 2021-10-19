'''
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
'''

class Node:

    def init(self, data):
        self.data = data
        self.next = None

class MyLinkedList:

    def init(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        temp = self.head
        i = 0
        while i < index:
            temp = temp.next
            i += 1
        return temp.data

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1


    def addAtTail(self, val: int) -> None:
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            self.size += 1
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        self.size += 1
        return 


    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        new_node = Node(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return 

        temp = self.head

        i = 1
        while i < index:
            temp = temp.next
            i += 1

        new_node.next = temp.next
        temp.next = new_node
        self.size += 1
        return

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        temp = self.head
        i = 1
        while i < index:
            temp = temp.next
            i += 1
        temp.next = temp.next.next
        self.size -= 1
        return
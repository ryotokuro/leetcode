# link: https://leetcode.com/problems/merge-two-sorted-lists/

# PROBLEM
# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.

# EXAMPLE
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    #def insert(self, data):


def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    head = tail = ListNode(0)

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2
    return head.next


l1 = ListNode(1)
l2 = ListNode(2)
l1.next = l2
node = l1.head
#l1.next.val = 2
#l1.next.next.val = 4

l2 = ListNode(1)
l2.val = 1
#l1.next.val = 3
#l1.next.next.val = 4
print(l1, l2.val)
mergeTwoLists(l1, l2)

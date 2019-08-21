# link: https://leetcode.com/problems/reverse-linked-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head: ListNode) -> ListNode:
    # METHOD 1: very simple with temp variable
    # if head is None:
    #     return head
    #
    # # set up
    # prev = None
    # curr = head
    # tmp = head.next
    #
    # while curr.next:
    #     curr.next = prev
    #     prev, curr, tmp = curr, tmp, tmp.next
    #
    # # once exited redirect the head
    # curr.next = prev
    # head = curr
    # return head

    # METHOD 2: no temp variables (Slightly less memory but same speed)
    new_head = None
    while head:
        head.next, head, new_head = new_head, head.next, head
    return new_head

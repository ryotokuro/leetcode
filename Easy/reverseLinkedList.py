# link:

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head: ListNode) -> ListNode:
    if head is None:
        return head

    # set up
    prev = None
    curr = head
    tmp = head.next

    while curr.next:
        curr.next = prev
        prev, curr, tmp = curr, tmp, tmp.next

    # once exited redirect the head
    curr.next = prev
    head = curr

    return head

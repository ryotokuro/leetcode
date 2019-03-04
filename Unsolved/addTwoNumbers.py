# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# EXAMPLE
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        string = None  # Have an empty string initially
        # Get linked list value and INSERT it (add to front) to a string
        print(l1.val)


aList = ListNode(2)
aList = aList.next
aList.val = 4
aList = aList.next
aList.val = 3

b = [5, 6, 4]

answer = Solution()
print(Solution.addTwoNumbers(answer, aList, b))


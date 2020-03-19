# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
        curr = l1
        num1 = []
        while curr:  # while curr is not not None/Null
            num1.append(curr.val)
            curr = curr.next
        
        curr = l2
        num2 = []
        while curr:  # while curr is not not None/Null
            num2.append(curr.val)
            curr = curr.next
            
        num1.reverse()
        num2.reverse()
        
        num1 = int(''.join(map(str, num1)))
        num2 = int(''.join(map(str, num2)))
        
        result = str(num1 + num2)
        result = list(result)
        result.reverse()
        
        l3 = ListNode(int(result.pop(0)))
        curr = l3
        while result:
            curr.next = ListNode(int(result.pop(0)))
            curr = curr.next
        
        return l3
    

def addTwoNumbers(l1, l2):
    l3 = None
    
    i = l1
    j = l2
    carry = 0
    while i or j:
        if i:
            d1 = i.val
        else:
            d1 = 0

        if j:
            d2 = j.val
        else:
            d2 = 0

        result = (d1 + d2 + carry) % 10
        carry = (d1 + d2 + carry) // 10
        result_node = ListNode(result)

        if i:
            i = i.next
        if j:
            j = j.next

        if not l3:
            l3 = result_node
            curr = l3
        else:
            curr.next = result_node
            curr = curr.next

    # Dangling remainder
    if carry == 1:
        curr.next = ListNode(1)
        
    return l3


# Test Cases
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
l1 = ListNode(2)
curr = l1
curr.next = ListNode(4)
curr = curr.next
curr.next = ListNode(3)

l2 = ListNode(5)
curr = l2
curr.next = ListNode(6)
curr = curr.next
curr.next = ListNode(4)

l3 = addTwoNumbers(l1, l2)
curr = l3
while curr:
    print(curr.val, end=' ')
    curr = curr.next
print()

# Edge Case: One List is longer than the other
# Input: (0 -> 1) + (0 -> 1 -> 2)
# Output: (0 -> 2 -> 2)
l1 = ListNode(0)
l1.next = ListNode(1)

l2 = ListNode(0)
curr = l2
curr.next = ListNode(1)
curr = curr.next
curr.next = ListNode(2)

l3 = addTwoNumbers(l1, l2)
curr = l3
while curr:
    print(curr.val, end=' ')
    curr = curr.next
print()

# Edge Case: One Empty Input
# Input: () + (0 -> 1)
# Output: (0 -> 1)
l1 = None

l2 = ListNode(0)
l2.next = ListNode(1)

l3 = addTwoNumbers(l1, l2)
curr = l3
while curr:
    print(curr.val, end=' ')
    curr = curr.next
print()

# Edge Case: Extra carry of 1
# Input: (9 -> 9) + (1)
# Output: (0 -> 0 -> 1)
l1 = ListNode(9)
l1.next = ListNode(9)

l2 = ListNode(1)

l3 = addTwoNumbers(l1, l2)
curr = l3
while curr:
    print(curr.val, end=' ')
    curr = curr.next

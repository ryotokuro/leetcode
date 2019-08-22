# link: https://leetcode.com/problems/delete-node-in-a-linked-list/

# PROBLEM
# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
#
# Given linked list -- head = [4,5,1,9], which looks like following:
# https://assets.leetcode.com/uploads/2018/12/28/237_example.png

# EXAMPLE
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation:
# - You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(self, node):
    tmp = node.next
    while tmp:
        node.val = tmp.val
        if tmp.next is not None:
            node = tmp
            tmp = tmp.next
        else:
            break
    node.next = None

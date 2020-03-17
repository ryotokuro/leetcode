# https://leetcode.com/problems/symmetric-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def isSymmetric(root):
        # Edge Case: Root is None
        if not root:
            return True

        # Edge Case: Root is only node in tree
        if not root.left:
            if not root.right:
                return True

        queue = [root]  # Stores upcoming nodes
        window = []  # Stores a 'window' consisting of all nodes from a given level at a time
        
        num_nodes = 0
        expected_nodes = 2  # The root node expects 2 child nodes
        actual_nodes = 0  # To count how manya nodes we actually encounter
        
        while queue:
            curr = queue.pop(0)
            
            if curr.left:
                queue.append(curr.left)
                window.append(curr.left.val)
                actual_nodes += 1
            else:
                window.append(None)

            if curr.right:
                queue.append(curr.right)
                window.append(curr.right.val)
                actual_nodes += 1
            else:
                window.append(None)

            num_nodes += 2
            if num_nodes == expected_nodes:
                # Verify the symmetry of nodes
                middle = len(window)//2
                if window[:middle] != list(reversed(window[middle:])):
                    # print("Broke at:", window)
                    return False            

                expected_nodes = actual_nodes*2  # calculate how many nodes we want in the next cycle
                num_nodes = 0
                actual_nodes = 0
                window = []

        return True


# TEST CASES
# [1, [2, 2], [3, 4, 4, 3]]
r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(2)
r.left.left = TreeNode(3)
r.left.right = TreeNode(4)
r.right.left = TreeNode(4)
r.right.right = TreeNode(3)
print(isSymmetric(r), "\n")

# [1, [2, None], [3, None, None, None]]
r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(None)
r.left.left = TreeNode(3)
print(isSymmetric(r), "\n")

# [1, [2, 2], [None, 3, 3, None]]
r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(2)
r.left.left = TreeNode(None)
r.left.right = TreeNode(3)
r.right.left = TreeNode(3)
r.right.right = TreeNode(None)
print(isSymmetric(r), "\n")

# [1, [2, 2], [None, 3, None, 3]]
r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(2)
r.left.left = TreeNode(None)
r.left.right = TreeNode(3)
r.right.left = TreeNode(None)
r.right.right = TreeNode(3)
print(isSymmetric(r), "\n")

# [2,3,3,4,null,null,4,null,5,5,null,null,6,6,null,7,8,8,7,9,0,0,1,1,0,0,9]
r = TreeNode(2)
r.left = TreeNode(3)
r.right = TreeNode(3)
r.left.left = TreeNode(4)
r.left.right = TreeNode(None)
r.right.left = TreeNode(None)
r.right.right = TreeNode(4)
r.left.left.left = TreeNode(None)
r.left.left.right = TreeNode(5)
r.right.right.left = TreeNode(5)
r.right.right.right = TreeNode(None)
print(isSymmetric(r))

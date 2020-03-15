# https://leetcode.com/problems/symmetric-tree/

# Strategy
# - start at root node
# - do bfs (breadth first search)
# - look at level on left and compare to level on right
# - if left is not the same as reverse(right)
#   > then return false
# - if you've gone through the whole tree then it must be true

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetric(root):
    # Edge Case: Tree is only 1 node
    if root:
        if not root.left:
            if not root.right:
                return True
    
    node = root
    queue = []
    
    level = 1  # Start from the second level
    numNodes = 2  # Second level has 2 nodes
    nodesAtLevel = []  # Stores the nodes on the given level
    
    while node:  # while node is not None
        #print("Level:", level, "Nodes left:", numNodes)
        
        if node.left:
            queue.append(node.left)
            nodesAtLevel.append(node.left.val)
        else:
            nodesAtLevel.append(None)
            
        if node.right:
            queue.append(node.right)
            nodesAtLevel.append(node.right.val)
        else:
            nodesAtLevel.append(None)

        if queue:
            node = queue.pop(0)
        else:
            break
        
        numNodes -= 2  # binary tree has 2 children
        
        if numNodes == 0:
            # If the current level is asymmetric
            #print(nodesAtLevel[:len(nodesAtLevel)//2], list(reversed(nodesAtLevel[len(nodesAtLevel)//2:]))) 
            if nodesAtLevel[:len(nodesAtLevel)//2] != list(reversed(nodesAtLevel[len(nodesAtLevel)//2:])):
                #print("Uneven:", nodesAtLevel)
                return False
            
            # Else, proceed onto the next level
            level += 1
            numNodes = pow(2, level)
            nodesAtLevel = []
        
    return True

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
print(isSymmetric(r))

#[2,3,3,4,null,null,4,null,5,5,null,null,6,6,null,7,8,8,7,9,0,0,1,1,0,0,9]

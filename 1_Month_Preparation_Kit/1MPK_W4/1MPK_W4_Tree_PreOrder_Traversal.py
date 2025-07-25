class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

## solution exploiting print end=" "
def preOrder(root):
    if root is None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


## solution with string accumulation
def acc_preOrder(root, isroot=True):
    if not root:
        return ""
    
    res = str(root.info)
    left_res = preOrder(root.left, False)
    right_res = preOrder(root.right, False)
    
    if left_res:
        res += " " + left_res
    if right_res:
        res += " " + right_res
    
    if isroot:
        print(res)
        return
    else:
        return res







tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

preOrder(tree.root)
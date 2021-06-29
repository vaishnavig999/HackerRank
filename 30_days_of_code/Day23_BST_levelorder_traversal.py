# Task
# A level-order traversal, also known as a breadth-first search, visits each level of a tree's nodes from left to right,
#  top to bottom. You are given a pointer, root, pointing to the root of a binary search tree. Complete the levelOrder 
#  function provided in your editor so that it prints the level-order traversal of the binary search tree.

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        
        queue = [root]
        while(queue):
            current = queue[0]
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            queue.pop(0)
            print(current.data,end=" ")

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)

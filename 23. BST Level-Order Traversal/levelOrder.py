import sys

class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data

class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data<= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):
        ### My Code Here ###

        if root == None:
            return
        queue_list = [root]
        while queue_list:
            cur_node = queue_list.pop(0)
            print(cur_node.data)
            if(cur_node.left!=None):
                queue_list.append(cur_node.left)
            if(cur_node.right!=None):
                queue_list.append(cur_node.right)

        ### My Code To Here ###

T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root,data)
myTree.levelOrder(root)
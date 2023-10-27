import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def constructBST(lst):
    l = len(lst)
    if l == 0 :
        return
    middle =  0
    if l %2 ==0:
        middle = l // 2-1
    else:
        middle = l // 2

    #middle = l // 2
    root = BinaryTreeNode(lst[middle])
    root.left =  constructBST(lst[0:middle])
    root.right = constructBST(lst[middle+1:])
    return root
def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root == None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)


# Main
n = int(input())
if (n > 0):
    lst = [int(i) for i in input().strip().split()]
else:
    lst = []
root = constructBST(lst)
preOrder(root)
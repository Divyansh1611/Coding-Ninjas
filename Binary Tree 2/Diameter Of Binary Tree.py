from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''
def height_and_diameter(root):
    if root is None:
        return 0, 0
    
    # Recursively compute height and diameter of left and right subtrees
    lh, ldiameter = height_and_diameter(root.left)
    rh, rdiameter = height_and_diameter(root.right)

    # Calculate the height of the current node's subtree
    h = 1 + max(lh, rh)

    # Calculate the diameter considering the current node
    current_diameter = max(lh + rh + 1, max(ldiameter, rdiameter))

    return h, current_diameter

# Main function to find the diameter of the binary tree
def diameterOfBinaryTree(root):
    _, diameter = height_and_diameter(root)
    return diameter

'''

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


def diameterOfBinaryTree(root):
    # Your code goes here
    if root is None:
        return 0

    lh = height(root.left)
    rh = height(root.right)

    ldiameter = diameterOfBinaryTree(root.left)
    rdiameter = diameterOfBinaryTree(root.right)

    return max(lh + rh + 1, max(ldiameter, rdiameter))


# Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    if length == 1:
        return None

    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root


def printLevelWise(root):
    if root == None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():

        while not inputQ.empty():

            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left != None:
                outputQ.put(curr.left)
            if curr.right != None:
                outputQ.put(curr.right)

        print()
        inputQ, outputQ = outputQ, inputQ


# Main
root = takeInput()

print(diameterOfBinaryTree(root))
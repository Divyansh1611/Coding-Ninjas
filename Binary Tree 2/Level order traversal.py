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
Sample Input 1:

10 20 30 40 50 -1 60 -1 -1 -1 -1 -1 -1 

Sample Output 1:

10 
20 30 
40 50 60 

'''

def printLevelWise(root):
    if root is None:
        return

    q = queue.Queue()
    q.put(root)
    q.put(None)
    while (not (q.empty())):
        curr = q.get()
        if curr is None:
            # If we encounter None, it means we have finished a level
            print()  # Print a line break to separate levels
            if not q.empty():
                q.put(None)  # Add the delimiter for the next level
        else:
            print(curr.data, end=" ")
            if curr.left is not None:
                q.put(curr.left)
            if curr.right is not None:
                q.put(curr.right)



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


# Main
root = takeInput()
printLevelWise(root)
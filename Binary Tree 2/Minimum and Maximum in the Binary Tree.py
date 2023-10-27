from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Representation of the Pair Class
class Pair:
    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum

'''
Sample Input 1:
8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
Sample Output 1:
1 14
'''

def find_max(root):
    if root is None:
        return 0
    max_val = root.data
    left_val = find_max(root.left)
    right_val = find_max(root.right)
    if left_val > max_val:
        max_val = left_val
    if right_val > max_val:
        max_val = right_val
    return max_val

def find_min(root):
    if root is None:
        return -1
    min_val = root.data
    lef = find_min(root.left)
    rig = find_min(root.right)
    if lef >= 0 and min_val > lef:
        min_val = lef # updated value
    if rig >= 0 and min_val > rig:
        min_val = rig # update for right vlaue
    return min_val


def getMinAndMax(root):
    if root is None:
        return
    maximum = find_max(root)
    minimum = find_min(root)
    res = Pair(minimum, maximum)
    return res



# Your code goes here


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
    if root is None:
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

pair = getMinAndMax(root)
print(str(str(pair.minimum) + " " + str(pair.maximum)))
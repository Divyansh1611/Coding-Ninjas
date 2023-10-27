import sys
from sys import stdin,setrecursionlimit,maxsize
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

'''
    larger = None
    if tree is None:
        return
    if tree.data > n:
        larger = tree.data

    for child in tree.children:
        res = nextLargest(child, n)

        if res.data > n and res.data <= larger.data:
            larger.data = res.data

    return larger
'''
def nextLargest(tree, n):
    larger = sys.maxsize
    if tree is None:
        return None

    if tree.data > n:
        larger = tree.data

    for child in tree.children:
        res = nextLargest(child, n)
        if res is not None and res > n and res <= larger:
            larger = res

    if larger == sys.maxsize:
        return None
    return larger



def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr = list(int(x) for x in stdin.readline().strip().split())
n = int(input())
tree = createLevelWiseTree(arr)
if nextLargest(tree, n):
    print(nextLargest(tree, n))
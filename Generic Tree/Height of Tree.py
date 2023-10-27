import sys

# main
sys.setrecursionlimit(10 ** 6)


## Read input as specified in the question.
## Print output as specified in the question.
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)


def height(root):
    if root is None:
        return 0
    ans = 0
    for child in root.children:
        childHeight = height(child)
        if childHeight > ans:
            ans = childHeight
    return ans + 1


def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i < size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0, childCount):
            temp = treeNode(int(arr[i + j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root


arr = list(int(x) for x in stdin.readline().rstrip().rsplit())
tree = createLevelWiseTree(arr)
print(heightOfTree(tree))
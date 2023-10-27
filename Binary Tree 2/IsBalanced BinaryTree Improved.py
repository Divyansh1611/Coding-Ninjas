class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printTree(root):
    if root is None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)

def printTreeDetailed(root):
    if root is None:
        return
    print(root.data, end=":")
    if root.left != None:
        print("L", root.left.data, end=",")
    if root.right != None:
        print("R", root.right.data, end="")
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

def treeInput():
    rootData=int(input())
    if rootData==-1:
        return None
    root=BinaryTreeNode(rootData)
    leftTree=treeInput()
    rightTree=treeInput()
    root.left=leftTree
    root.right=rightTree
    return root

def height(root):
    if root==None:
        return 0
    return 1+max(height(root.left), height(root.right))

def isBalanced(root):
    if root==None:
        return True
    lh=height(root.left)
    rh=height(root.right)
    if lh-rh>1 or rh-lh>1:
        return False
    isLeftBalanced=isBalanced(root.left)
    isRightBalanced=isBalanced(root.right)
    if isLeftBalanced and isRightBalanced:
        return True
    else:
        return False

def getHeightAndCheckBalanced(root):
    if root == None:
        return 0, True

    lh, isLeftBalanced = getHeightAndCheckBalanced(root.left)
    rh, isRightBalanced = getHeightAndCheckBalanced(root.right)

    h = 1+max(lh,rh)
    if lh-rh > 1 or rh-lh > 1:
        return h, False
    if isLeftBalanced or isRightBalanced :
        return h, True
    else :
        return h, False

def isBalanced2(root):
    h,isRootBalanced = getHeightAndCheckBalanced(root)
    return h,False

root=treeInput()
printTreeDetailed(root)
print(getHeightAndCheckBalanced(root))
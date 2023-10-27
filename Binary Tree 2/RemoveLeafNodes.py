

def Remove(root):

    if root is None:
        return None
    if root.left == None and root.right == None:
        return None

    root.left = Remove(root.left)
    root.right = Remove(root.right)
    return root

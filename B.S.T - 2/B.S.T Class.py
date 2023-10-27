class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:

    def __init__(self):
        self.root = None
        self.numNodes = 0

    def printTree(self):
        self._print_recursive(self.root)

    def _print_recursive(self, node):
        if node is None:
            return

        output = f"{node.data}:"

        # Check and add left child if not null
        if node.left:
            output += f"L:{node.left.data},"

        # Check and add right child if not null
        if node.right:
            output += f"R:{node.right.data},"

        # Remove the trailing comma if it exists
        if output[-1] == ",":
            output = output[:-1]

        # Print the final output
        print(output)

        # Recursively process left and right subtrees
        self._print_recursive(node.left)
        self._print_recursive(node.right)


    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)

    def insert(self, data):
        self.root = self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if node is None:
            self.numNodes += 1
            return BinaryTreeNode(data)
        if data == node.data:
            node.left = self._insert_recursive(node.left, data)
        elif data < node.data:
            node.left = self._insert_recursive(node.left, data)
        else:
            node.right = self._insert_recursive(node.right, data)
        return node

    def delete(self, data):
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, node, data):
        if node is None:
            return node
        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.data = self._min_value(node.right)
            node.right = self._delete_recursive(node.right, node.data)
        return node

    def _min_value(self, node):
        while node.left is not None:
            node = node.left
        return node.data

    def count(self):
        return self.numNodes


b = BST()
q = int(input())
while (q > 0):
    li = [int(ele) for ele in input().strip().split()]
    choice = li[0]
    q -= 1
    if choice == 1:
        data = li[1]
        b.insert(data)
    elif choice == 2:
        data = li[1]
        b.delete(data)
    elif choice == 3:
        data = li[1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
    else:
        b.printTree()
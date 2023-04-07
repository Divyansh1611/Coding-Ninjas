from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def helper(head, n, i):
    if (not head):
        return -1

    if head.data == n:
        return i

    recall = helper(head.next, n, i + 1)
    return recall


def findNodeRec(head, n):
    i = 0
    res = helper(head, n, i)
    return res


def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head


def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    n = int(stdin.readline().rstrip())

    print(findNodeRec(head, n))

    t -= 1
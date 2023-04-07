from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def mergeSort(head):
    if head is None:
        return

    if (head.next == None):
        return head

    mid = findMid(head)
    head2 = mid.next
    mid.next = None
    newHead1 = mergeSort(head)
    newHead2 = mergeSort(head2)
    finalHead = merge(newHead1, newHead2)
    return finalHead


def merge(head1, head2):
    merged = Node(-1)

    temp = merged
    # While head1 is not null and head2
    # is not null
    while (head1 != None and head2 != None):
        if (head1.data < head2.data):
            temp.next = head1
            head1 = head1.next
        else:
            temp.next = head2
            head2 = head2.next
        temp = temp.next

    # While head1 is not null
    while (head1 != None):
        temp.next = head1
        head1 = head1.next
        temp = temp.next

    # While head2 is not null
    while (head2 != None):
        temp.next = head2
        head2 = head2.next
        temp = temp.next

    return merged.next


# Find mid using The Tortoise and The Hare approach
def findMid(head):
    slow = head
    fast = head.next
    while (fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
    return slow


# Taking Input Using Fast I/O
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

    newHead = mergeSort(head)
    printLinkedList(newHead)

    t -= 1
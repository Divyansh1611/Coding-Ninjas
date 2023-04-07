from sys import stdin


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def listLength(head):
    counter = 0
    while head is not None:
        counter += 1
        head = head.next
    return counter

# def midPoint(head):
#     mid = (listLength(head) - 1) // 2
#     i = 0
#     while head is not None:
#         if i == mid:
#             return head
#         i = i +1
#         head = head.next
#     return head

'''OR
1
1 2 3 4 5 -1
'''
def midPoint(head):

    pass

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


# Main
t = int(stdin.readline().rstrip())

while t > 0:

    head = takeInput()
    mid = midPoint(head)

    if mid is not None:
        print(mid.data)

    t -= 1
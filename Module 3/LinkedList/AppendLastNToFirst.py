
from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def LengthLinkedList(head):
    counter = 0
    while head is not None:
        counter = counter + 1
        head = head.next
    return counter

def reCall(head,n):
    if n == 1:
        temp = head.next
        head.next = None
        return temp
    return reCall(head.next, n-1)

def appendN(head, temp):
    if head is None:
        print(head.data)
        head.next = temp
    return (head.next, temp)

def appendLastNToFirst(head, n):
    length = LengthLinkedList(head)
    if n == 0:
        return head
    if n > length:
        return
    n = reCall(head, length - n)
    temp = n
    while temp.next is not None:
        temp = temp.next
    temp.next = head
    return n

#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head


#to print the linked list
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    head = takeInput()
    n = int(stdin.readline().rstrip())

    head = appendLastNToFirst(head, n)
    printLinkedList(head)

    t -= 1
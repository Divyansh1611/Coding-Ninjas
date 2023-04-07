from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def findNode(head, n) :
    index = 0
    while head is not None:
        if head.data == n :
            return index
        index = index + 1
        head = head.next
    return -1
    pass

''' Recursively
def findNode(head, n) :
    if head is None:
        return -1
    if head.data == n:
        return 0
    index = findNode(head.next, n)
    return (1 + index) if index != -1 else -1
'''

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

# Main.
t = int(stdin.readline().rstrip())
while t > 0 : 
    head = takeInput()
    n = int(stdin.readline().rstrip())
    print(findNode(head, n))
    t -= 1
from sys import stdin

'''
Sample Input 1 :
13
2 12 9 16 10 5 3 20 25 11 1 8 6
 
Sample Output 1 :
8 12 
Explanation:The longest consecutive sequence here is [8, 9, 10, 11, 12]. So the output is the start and end of this sequence: [8, 12].
'''
def longestConsecutiveSubsequence(arr, n):
    numSet =  set(arr)
    longest  = 0
    start = end = 0
    for n in arr:
        # check if its the start of a sequence

        if (n-1) not in numSet:
            lenght =0
            while (n+lenght) in numSet:
                lenght +=1
            if lenght > longest:
                start = n
                end = n + lenght-1
            longest = max(longest,lenght)
    return (start,end)


def takeInput():
    # To take fast I/O
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split()))
    return arr, n


# Main
arr, n = takeInput()
ans = longestConsecutiveSubsequence(arr, n)
# This ans array contains two numbers, ie, start and end of longest sequence respectively
print(*ans)
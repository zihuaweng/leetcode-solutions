"""
https://songlee24.github.io/2014/04/09/matrix-transpose-inplace/

arr = [1,2,3,4,5,6,7, 8]
m = 4
n = 2

matrix m * n 

transpose:
        m * n -> n * m
        (i, j) -> (j, i)

cur index : i  
    cur location (i//n, i%n)
    next location (i%n, i//n)
    next index : (i%n)*m + i//n

next index: i
    next location (i%m, i//m)
    cur location (i//m, i%m)
    cur index : (i%m)*n + i//m


it will have cycle
check out the link for details

0 -> 0
1 -> 4 -> 2 -> 1
2 -> 1 -> 4 -> 2 (duplecated)
3 -> 5 -> 6 -> 3
4 -> 2 -> 1 -> 4 (duplecated)
5 -> 6 -> 3 -> 5 (duplecated)
6 -> 3 -> 5 -> 6 (duplecated)
7 -> 7

"""

def get_prev(i, m, n):
    return (i%m)*n + i//m

def get_next(i, m, n):
    return (i%n)*m + i//n

def move_num(arr, i, m, n):
    temp = arr[i]
    cur = i
    prev = get_prev(i, m, n)
    while prev != i:
        arr[cur] = arr[prev]
        cur = prev
        prev = get_prev(prev, m, n)

    arr[cur] = temp

# find the cycle and move nums
def transpose(arr, m, n):
    for i in range(len(arr)):
        nxt = get_next(i, m, n)
        while nxt > i:
            nxt = get_next(nxt, m, n)
        if nxt == i:
            move_num(arr, i, m, n)

    return arr

print(transpose([1,2,3,4,5,6,7, 8], 4 , 2))

        

        
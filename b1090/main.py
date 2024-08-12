import sys
import heapq as pq

sys.stdin = open("input.txt", "r")


import math

N = int(input())
X = []
Y = []
arr = []
for i in range(N):
    x,y = map(int, input().split())
    X.append(x)
    Y.append(y)
    arr.append([x,y])

result = [math.inf] * N

for x in X:
    for y in Y:
        tmp = []
        for l in arr:
            tmp.append(abs(l[0]- x) + abs(l[1] - y) )
        tmp = sorted(tmp)
        
        for i in range(len(tmp)):
            s = sum(tmp[:i+1])
            if result[i] > s:
                result[i] = s
    
print(*result)
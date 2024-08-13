import sys

sys.stdin = open("input.txt", "r")

result = []
arr = []

N = int(input())

for i in range(N):
    a,b = map(int,input().split())
    arr.append([a,b])
    
for a in range(N):
    cnt = 1
    for b in range(N):
        if arr[a][0] < arr[b][0] and arr[a][1] < arr[b][1]:
            cnt+=1
    result.append(cnt)

print(*result)


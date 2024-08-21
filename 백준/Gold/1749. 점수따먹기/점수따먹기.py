import sys

N,M = map(int, sys.stdin.readline().split())
m = -999999999
arr = [0] * N
sumArr  = [[0 for _ in range(M+1)] for _ in range(N+1)]
for i in range(N):
    arr[i] = list(map(int, sys.stdin.readline().split()))
    for k in range(M):
        m = max(m, arr[i][k])

for a in range(1, N+1):
    for b in range(1, M+1):
        sumArr[a][b] = sumArr[a-1][b] + sumArr[a][b-1] + arr[a-1][b-1] - sumArr[a-1][b-1]
        m = max(m, sumArr[a][b])



for a in range(N+1):
    for b in range(M+1):
        for c in range(a):
            for d in range(b):
                m = max(m, sumArr[a][b] + sumArr[c][d] - sumArr[a][d] - sumArr[c][b])

print(m)
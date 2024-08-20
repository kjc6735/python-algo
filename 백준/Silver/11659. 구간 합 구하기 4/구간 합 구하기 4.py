import sys

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
sum_arr = [0] * (N+1)

for i,v in enumerate(arr):
    sum_arr[i+1] = arr[i] + sum_arr[i]

for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    print(sum_arr[E] - sum_arr[S-1])


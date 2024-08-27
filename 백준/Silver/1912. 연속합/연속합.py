import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = -999999999
sum = 0
for i in arr:
    m = max(m, i)
    if(sum + i >= 0):
        sum += i
        m = max(m, sum)
    else:
        sum = 0

print(m)



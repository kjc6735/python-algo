import sys
read = sys.stdin.readline

N = int(read())
arr = sorted(map(int, read().split()))
x = int(read())

s = 0
e = N-1
cnt = 0
while(s < e):
    if arr[s] + arr[e] == x:
        cnt+=1
        s +=1
        e -=1
    elif arr[s] + arr[e] < x:
        s += 1
    else:
        e-=1
print(cnt)


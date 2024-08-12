import sys

sys.stdin = open("input.txt", "r")

N = int(input())
x = []
y = []
arr = []
for i in range(N):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)
    arr.append([a,b])

x = sorted(x)
y = sorted(y)
x_center = x[ (N-1) // 2 ]
y_center = y[ (N-1) // 2 ]
distance = 0

for i in range(N):
    distance += abs(x_center - arr[i][0]) + abs(y_center - arr[i][1])

print(distance)
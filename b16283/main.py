
import sys

sys.stdin = open("input.txt", "r")


a,b,n,w = map(int, input().split())

result = []
for i in range(1, n):
    if(a*i + b*(n-i) == w):
        result.append(i)
        result.append(n-i)

if(len(result) == 2):
    print("{} {}".format(result[0], result[1]))
else: 
    print(-1)
    

import sys

sys.stdin = open("input.txt", "r")

def calc(num):
    num_str = str(num)
    s = sum(int(a) for a in num_str)
    return num + s


visited = [False] * 10001
result = []
for i in range(1, 10001):
    tmp = i
    if visited[tmp] == False:
        result.append(tmp)
    while tmp < 10001 :
        visited[tmp] = True
        tmp = calc(tmp)

for i in result:
    print(i)